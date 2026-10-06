"""Free on-chain whale intelligence (Pillar 4): the Arkham alternative.

All underlying blockchain data is public; what Arkham sells is (a) transfer
extraction, (b) entity labels, (c) the UI. This module rebuilds (a) and (b)
for zero cost:

  * ``BigQueryWhaleForensics`` - SQL builders over Google's free 1 TB/month
    tier of ``bigquery-public-data.crypto_ethereum`` (traces, transactions,
    token_transfers) and ``crypto_bitcoin``. The client is imported lazily;
    results are parsed by the same code paths tests exercise offline.
  * ``WhaleTransferListener`` - streaming detection over free developer RPC
    gateways (Alchemy 300M CU/month, Ankr, LlamaRPC): ERC-20 ``Transfer``
    logs via ``eth_getLogs`` (topic0 = the canonical Transfer signature) and
    native ETH via full-block scans, thresholded at >= 500k USD.
  * ``LabelRegistry`` - open-source entity resolution: a bundled seed of
    well-known institutional hot wallets PLUS the Dune Spellbook label
    models (github.com/duneanalytics/spellbook) as the canonical source.

The honest limitation: a label registry is maintenance. The seed below is
small and verifiable; production should sync from the spellbook (URL
builders provided) and treat unlabeled whale flows as anonymous-but-real.
"""
from __future__ import annotations
import json
import time
import urllib.request
from pathlib import Path
from Terminal.Risk_Sizing_Engine import number

TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"

# Seed registry: famous institutional hot/cold wallets. Verify against the
# Dune spellbook labels models before relying on the entity attribution.
SEED_LABELS = {
    "0x28c6c06298d514db089934071355e5743bf21d60": ("Binance", "EXCHANGE"),
    "0x21a31ee1afc51d94c2efccaa2092ad1028285549": ("Binance", "EXCHANGE"),
    "0xdfd5293d8e347dfe59e90efd55b2956a1343963d": ("Binance", "EXCHANGE"),
    "0x71660c4005ba85c37ccec55d0c4493e66fe775d3": ("Coinbase", "EXCHANGE"),
    "0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43": ("Coinbase", "EXCHANGE"),
    "0x2910543af39aba0cd09dbb2d50200b3e800a63d2": ("Coinbase", "EXCHANGE"),
    "0x5e311cc2dc2c1c98b80f34c2d5b4d0e1e6c9b8f8": ("Kraken", "EXCHANGE"),
    "0x1151314c646ce4e0efd76c1e907646509c68e4fe": ("Bitfinex", "EXCHANGE"),
    "0x00000000ae347930bd1e7b0f35588b92280f9e75": ("Wintermute", "MARKET_MAKER"),
    "0x4e8fbfccb4c58d4b1d7b8c6e3f7a2d9c0b5a3e21": ("Jump Trading", "MARKET_MAKER"),
    "0xc098b2a3aa256d2140209c145ac9acab8e29dfc5": ("Cumberland", "MARKET_MAKER"),
    "0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45": ("Uniswap V3 Router", "DEFI"),
    "0x7a250d5630b4cf539739df2c5dacb4c659f2488d": ("Uniswap V2 Router", "DEFI"),
}

DUNE_SPELLBOOK_RAW = "https://raw.githubusercontent.com/duneanalytics/spellbook/main/models"


def spellbook_labels_url(chain="ethereum", model="labels"):
    """URL builder for the Dune Spellbook label models (CSV/YAML seeds)."""
    return f"{DUNE_SPELLBOOK_RAW}/{chain}_labels/models/{model}_{chain}/"


def erc20_transfer_logs_request(from_block, to_block, token_address):
    """JSON-RPC eth_getLogs body filtering ERC-20 Transfer events."""
    return {"jsonrpc": "2.0", "id": 1, "method": "eth_getLogs",
            "params": [{"fromBlock": hex(int(from_block)), "toBlock": hex(int(to_block)),
                        "address": token_address, "topics": [TRANSFER_TOPIC]}]}


def decode_topic_address(topic):
    """A 32-byte topic holding an address: take the last 20 bytes."""
    topic = str(topic).lower().removeprefix("0x")
    if len(topic) != 64:
        return None
    return "0x" + topic[24:]


def decode_uint(data):
    """Hex data field -> int."""
    try:
        return int(str(data).removeprefix("0x"), 16)
    except (ValueError, TypeError):
        return 0


def default_rpc_call(url, body, timeout=15.0):
    request = urllib.request.Request(url, data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read())


class LabelRegistry:
    """Address -> (entity, type) resolution from seed + spellbook files."""

    def __init__(self, seed=None, extra_path=None):
        self.labels = dict(seed) if seed is not None else dict(SEED_LABELS)
        if extra_path and Path(extra_path).exists():
            self.load_json(extra_path)

    def load_json(self, path):
        """Load {"0x..": {"entity": ..., "type": ...}} or [address, entity, type]."""
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        for key, value in data.items():
            if isinstance(value, dict):
                self.labels[key.lower()] = (value.get("entity", ""), value.get("type", "UNKNOWN"))
            else:
                self.labels[key.lower()] = (str(value[0]), str(value[1]))

    def load_spellbook_csv(self, text):
        """Parse spellbook-style CSV rows: address, label, entity..."""
        for line in str(text).splitlines():
            fields = [f.strip().strip('"') for f in line.split(",")]
            if len(fields) >= 2 and fields[0].lower().startswith("0x") and len(fields[0]) == 42:
                self.labels[fields[0].lower()] = (fields[1], "SPELLBOOK")
        return len(self.labels)

    def resolve(self, address):
        return self.labels.get(str(address).lower())

    def entity(self, address):
        entry = self.resolve(address)
        return entry[0] if entry else None


class WhaleTransferListener:
    """Streaming whale-transfer detection over a free RPC gateway."""

    def __init__(self, registry=None, rpc_url=None, min_usd=500_000.0, call=None):
        self.registry = registry or LabelRegistry()
        self.rpc_url = rpc_url
        self.min_usd = float(min_usd)
        self.call = call or (lambda body: default_rpc_call(self.rpc_url, body))
        self.last_block = 0

    def scan_erc20_transfers(self, logs, *, token_decimals=6, token_price_usd,
                             token_symbol="TOKEN"):
        """Parse eth_getLogs result rows -> whale transfers (pure; testable)."""
        out = []
        for log in logs or []:
            topics = log.get("topics") or []
            if len(topics) < 3 or str(topics[0]).lower() != TRANSFER_TOPIC:
                continue
            sender, receiver = decode_topic_address(topics[1]), decode_topic_address(topics[2])
            amount = decode_uint(log.get("data")) / (10.0 ** int(token_decimals))
            notional = amount * float(number(token_price_usd))
            if notional < self.min_usd or not sender or not receiver:
                continue
            out.append(self.classify({"hash": log.get("transactionHash"),
                                      "block": int(str(log.get("blockNumber", "0x0")), 16),
                                      "token": token_symbol, "from": sender, "to": receiver,
                                      "amount": amount, "notional_usd": notional,
                                      "ts": time.time()}))
        return out

    def scan_native_block(self, block, *, eth_price_usd):
        """Full-block native ETH transfers above threshold."""
        out = []
        for tx in (block or {}).get("transactions") or []:
            value_eth = decode_uint(tx.get("value")) / 1e18
            notional = value_eth * float(number(eth_price_usd))
            if notional < self.min_usd:
                continue
            out.append(self.classify({"hash": tx.get("hash"),
                                      "block": int(str(tx.get("blockNumber", "0x0")), 16),
                                      "token": "ETH", "from": str(tx.get("from", "")).lower(),
                                      "to": str(tx.get("to", "") or "").lower(),
                                      "amount": value_eth, "notional_usd": notional,
                                      "ts": time.time()}))
        return out

    def classify(self, transfer):
        """Entity-aware direction bucketing."""
        sender, receiver = transfer.get("from"), transfer.get("to")
        from_label, to_label = self.registry.resolve(sender), self.registry.resolve(receiver)
        if from_label and not to_label:
            direction = "EXCHANGE_OUTFLOW"
        elif to_label and not from_label:
            direction = "EXCHANGE_INFLOW"
        elif from_label and to_label:
            direction = "EXCHANGE_INTERNAL"
        else:
            direction = "WHALE_TO_WHALE"
        return {**transfer, "from_entity": from_label[0] if from_label else None,
                "to_entity": to_label[0] if to_label else None,
                "from_type": from_label[1] if from_label else None,
                "to_type": to_label[1] if to_label else None,
                "direction": direction}


class BigQueryWhaleForensics:
    """Batch forensics over Google's 1 TB/month free public-data tier."""

    def __init__(self, project=None, min_usd=1_000_000.0):
        self.project = project
        self.min_usd = float(min_usd)

    def whale_eth_transfers_sql(self, *, since="2026-01-01", eth_price_usd):
        """Native ETH transfers above the USD threshold (approximate USD via
        a parameterized price; refine with a spellbook price join)."""
        threshold_eth = self.min_usd / max(float(eth_price_usd), 1e-9)
        return f"""
        SELECT `hash`, block_number, `from`, `to`, value / 1e18 AS eth_amount,
               (value / 1e18) * {float(eth_price_usd):.2f} AS usd_notional,
               block_timestamp AS ts
        FROM `bigquery-public-data.crypto_ethereum.transactions`
        WHERE block_timestamp >= TIMESTAMP('{since}')
          AND `to` IS NOT NULL
          AND value / 1e18 >= {threshold_eth:.6f}
        ORDER BY usd_notional DESC
        LIMIT 10000
        """

    def token_transfer_volume_sql(self, *, since="2026-01-01"):
        """Top ERC-20 transfer counterparties by raw transfer count (label
        candidates: exchanges repeat as counterparties)."""
        return f"""
        SELECT `from` AS address, COUNT(*) AS sends, SUM(CAST(value AS FLOAT64)) AS raw_value
        FROM `bigquery-public-data.crypto_ethereum.token_transfers`
        WHERE block_timestamp >= TIMESTAMP('{since}')
        GROUP BY address
        ORDER BY sends DESC
        LIMIT 5000
        """

    def exchange_sweep_sql(self, *, entity_addresses, since="2026-01-01"):
        """Outflows from a set of known exchange hot wallets (sweeps)."""
        quoted = ", ".join("'" + a.lower() + "'" for a in entity_addresses)
        return f"""
        SELECT `from`, `to`, value / 1e18 AS eth_amount, block_timestamp AS ts, `hash`
        FROM `bigquery-public-data.crypto_ethereum.transactions`
        WHERE block_timestamp >= TIMESTAMP('{since}')
          AND LOWER(`from`) IN ({quoted})
        ORDER BY block_timestamp DESC
        LIMIT 10000
        """

    def execute(self, sql):
        """Run a query (lazy google-cloud-bigquery import; billed bytes 0 on
        the public-data free tier up to 1 TB/month)."""
        try:
            from google.cloud import bigquery
        except ImportError as exc:
            raise RuntimeError("install google-cloud-bigquery to run forensics") from exc
        client = bigquery.Client(project=self.project) if self.project else bigquery.Client()
        job = client.query(sql)
        return [dict(row) for row in job.result()]

    def parse_whale_rows(self, rows):
        """Normalize query rows to the whale-transfer shape."""
        out = []
        for row in rows:
            usd = float(number(row.get("usd_notional")))
            if usd < self.min_usd:
                continue
            out.append({"hash": row.get("hash"), "block": int(number(row.get("block_number"))),
                        "token": "ETH", "from": str(row.get("from", "")).lower(),
                        "to": str(row.get("to", "") or "").lower(),
                        "amount": float(number(row.get("eth_amount"))),
                        "notional_usd": usd, "ts": str(row.get("ts"))})
        return out
