# OMNI explicit return and exception branch review

This companion maps every explicit return, raise and exception handler in the thirteen audited files to its function-level disposition. The full inventory additionally contains if/conditional-expression/break/continue nodes. Syntax enumeration is not exhaustive runtime path coverage. Long expressions below are abbreviated for readability; the JSON inventory preserves them without abbreviation. All referenced sources are hashed in that inventory.

## Terminal/Api_Client.py

### HyperdashClient._post_json

Limiter waits before HTTP; provider/GraphQL errors raise wrapped RuntimeError. Shared limiter is locked, but waits can accumulate and client caches are not synchronized.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [45](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:45) | Raise | isinstance(result, dict) and result.get('errors') | ValueError(f"GraphQL rejected request: {result['errors']}") |
| [46](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:46) | Return | No enclosing if; see source try/loop/call context | result |
| [47](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:47) | ExceptHandler | No enclosing if; see source try/loop/call context | urllib.error.HTTPError |
| [49](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:49) | Raise | No enclosing if; see source try/loop/call context | RuntimeError(f'HTTP {e.code} Error from {url}: {err_msg}') |
| [50](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:50) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [51](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:51) | Raise | No enclosing if; see source try/loop/call context | RuntimeError(f'Connection Error to {url}: {e}') |

### HyperdashClient._resolve_coin

Qualified coin returns directly; known legacy assets require observed cache/metadata mapping or raise. Crypto returns canonical asset. No invented HIP-3 fallback.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [129](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:129) | Return | ':' in coin | coin |
| [137](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:137) | Raise | asset in {'SP500', 'NAS100', 'DJ30', 'GOLD', 'SILVER'} AND not cached or not cached.get('signal_market') | ValueError(f'No observed HIP-3 market for {asset}') |
| [138](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:138) | Return | asset in {'SP500', 'NAS100', 'DJ30', 'GOLD', 'SILVER'} | cached['signal_market'] |
| [139](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:139) | Return | No enclosing if; see source try/loop/call context | asset |

### HyperdashClient.download_historical_candles

Offline archive download, no broker order effect. Returns stored provider history/metadata; this alone does not validate live microstructure or uplift labels.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [658](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:658) | Raise | not all_candles | RuntimeError(f'No candles retrieved for {coin}') |
| [681](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:681) | Return | No enclosing if; see source try/loop/call context | str(file_path) |

### HyperdashClient.download_historical_funding

Offline funding archive, no broker order effect. Returned history is not a trade outcome or counterfactual target.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [704](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:704) | Raise | not records | RuntimeError(f'No funding records found for {coin}') |
| [719](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:719) | Return | No enclosing if; see source try/loop/call context | str(file_path) |

### HyperdashClient.fetch_all_assets

Main universe failure propagates; xyz/flx failures are suppressed and return partial observed universe. Canonical duplicates pick first observed market; listing identity/units not independently pinned.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [70](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:70) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [81](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:81) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [126](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:126) | Return | No enclosing if; see source try/loop/call context | results |

### HyperdashClient.fetch_candles

Research/history chart returns candles or error fallback; not the live broker completed-bar filter. Scratch covariance script must exclude the current candle separately.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [613](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:613) | Return | No enclosing if; see source try/loop/call context | candles |

### HyperdashClient.fetch_l2_book

Returns top twenty sides/event and receipt time, or propagates provider/parse failure. Top twenty depth does not cover arbitrary liquidation corridors.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [163](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:163) | Return | No enclosing if; see source try/loop/call context | {'coin': coin, 'signal_market': hl_coin, 'best_bid': best_bid, 'best_ask': best_ask, 'spread': spread, 'spread_bps': spread_bps, 'bids': bids, 'asks': asks, 'bid_volume_usd': bid_vol, 'ask_volume_usd': ask_vol, 'bid_pct': bid_ratio, 'ask_pct': 100.0 - bid_ratio, 'timestamp': raw.get('time', 0), 'received_at': time.time()} |

### HyperdashClient.fetch_l3_orders

Returns wallet-labelled sorted order clusters with receipt-only time; GraphQL omits stable order ID/event timestamp. Upstream errors propagate to server retention branch.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [221](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:221) | Return | No enclosing if; see source try/loop/call context | orders |

### HyperdashClient.fetch_liquidations

Returns provider landscape/realized summary, not projected wallet exposure. Server labels/retains it; quantitative scorer admits only explicit exposure/stop kinds. Historical fetch errors may be suppressed as fallback result.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [320](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:320) | ExceptHandler | No enclosing if; see source try/loop/call context | (ValueError, TypeError, OSError) |
| [338](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:338) | Return | No enclosing if; see source try/loop/call context | {'coin': coin, 'current_price': res.get('currentPrice', 0.0), 'kind': 'UNVERIFIED_BAND_LANDSCAPE', 'received_at': time.time(), 'band_size': res.get('bandSize', 100.0), 'total_long_size': res.get('totalLongLiquidations', {}).get('size', 0.0), 'total_long_count': res.get('totalLongLiquidations', {}).get('count', 0), 'total_short_size': res. … (full expression in JSON) |

### HyperdashClient.fetch_recent_trades

Returns provider prints or a failure fallback according to listed branch; server formats side/time/size and deduplicates IDs in scoring. Missing tape is a neutral score, not evidence of no aggressor flow.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [533](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:533) | Return | No enclosing if; see source try/loop/call context | trades if trades else [] |
| [534](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:534) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [535](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:535) | Return | No enclosing if; see source try/loop/call context | [] |

### HyperdashClient.fetch_stops

Returns provider stop landscape summary or fallback branch. Quantitative use requires explicit observed semantics and fresh component provenance.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [455](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:455) | ExceptHandler | No enclosing if; see source try/loop/call context | (ValueError, TypeError, OSError) |
| [473](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:473) | Return | No enclosing if; see source try/loop/call context | {'coin': coin, 'current_price': res.get('currentPrice', 0.0), 'band_size': res.get('bandSize', 100.0), 'total_buy_size': res.get('totalBuyStops', {}).get('size', 0.0), 'kind': 'UNVERIFIED_STOP_LANDSCAPE', 'received_at': time.time(), 'total_buy_count': res.get('totalBuyStops', {}).get('count', 0), 'total_sell_size': res.get('totalSellStops … (full expression in JSON) |

### HyperdashClient.fetch_top_traders

UI/research cohort query; error/fallback does not provide total market leverage. Not used as global position inventory.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [525](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:525) | Return | No enclosing if; see source try/loop/call context | positions |

### HyperdashClient.fetch_wallet_risk

Recent cache returns early; otherwise at most two addresses supply positions/explicit reduce-only stops and projected corridors. HTTP failures propagate. Entire position notional is scenario exposure, not measured liquidation volume.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [546](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:546) | Return | cache and now - cache['observed_at'] < 30 | cache |
| [584](C:/Users/SIGMA/Documents/Trading_2/Terminal/Api_Client.py:584) | Return | No enclosing if; see source try/loop/call context | result |

## Terminal/Asset_Universe.py

### broker_candidates

Returns ordered known base/suffix combinations; resolver must observe exact match. Sixteen entries in UNIVERSE do not prove sixteen live markets.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [25](C:/Users/SIGMA/Documents/Trading_2/Terminal/Asset_Universe.py:25) | Return | No enclosing if; see source try/loop/call context | [base + suffix for base in bases for suffix in ('.p', '.pi', '', '.a', 'm')] |

### canonical_asset

Returns explicit aliases/base crypto or unchanged normalized name; unknown symbols are not magically tradable. Prefix/decimal suffix stripping needs an explicit instrument contract for unusual broker names.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [14](C:/Users/SIGMA/Documents/Trading_2/Terminal/Asset_Universe.py:14) | Return | name in ALIASES | ALIASES[name] |
| [17](C:/Users/SIGMA/Documents/Trading_2/Terminal/Asset_Universe.py:17) | Return | name.endswith(suffix) and name[:-len(suffix)] in UNIVERSE | name[:-len(suffix)] |
| [18](C:/Users/SIGMA/Documents/Trading_2/Terminal/Asset_Universe.py:18) | Return | No enclosing if; see source try/loop/call context | {'DOGUSD': 'DOGE', 'LNKUSD': 'LINK'}.get(name, name) |

## Terminal/Chrome_Terminal.py

### _refresh_analytics_worker

Each component exception retains prior values; successful empty L3 clears prior walls. Complete cache replacement then refreshing marker cleared in finally. Cold duplicate workers and out-of-order completion are possible; retained source timestamps help detect old components.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [147](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:147) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [203](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:203) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [252](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:252) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [260](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:260) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [268](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:268) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |

### api_cohorts

UI cohort request returns provider result or HTTP error; not global leverage truth.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [464](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:464) | Return | No enclosing if; see source try/loop/call context | {'coin': coin, 'cohorts': cohorts} |
| [465](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:465) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [466](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:466) | Return | No enclosing if; see source try/loop/call context | {'coin': coin, 'cohorts': [], 'error': str(e)} |

### api_heatmap

UI/research request returns heatmap or HTTP error; not the trader live feature path.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [408](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:408) | Return | No enclosing if; see source try/loop/call context | payload |
| [409](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:409) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [410](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:410) | Raise | No enclosing if; see source try/loop/call context | HTTPException(status_code=500, detail=str(e)) |

### api_live

Unknown coin raises HTTP404. Book exception produces missing/error book; tape exception empties tape. Synchronous first analytics load can outlast local client timeout. Response time does not establish each component freshness.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [312](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:312) | Raise | not meta | HTTPException(status_code=404, detail=f'Asset {coin} not found in universe') |
| [325](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:325) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [329](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:329) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [381](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:381) | Return | No enclosing if; see source try/loop/call context | {'coin': coin, 'price': live_px, 'meta': meta, 'signal_market': meta.get('signal_market'), 'sources': {**analytics.get('sources', {}), 'l2': {'observed_at': l2_book.get('timestamp', 0), 'timestamp_basis': 'VENUE_EVENT_TIME'}}, 'whale_positions': analytics.get('wallet_risk', {}).get('positions', []), 'projected_liquidations': analytics.get … (full expression in JSON) |

### api_universe

Returns current universe or upstream failure; no orders.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [304](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:304) | Return | No enclosing if; see source try/loop/call context | {'count': len(assets), 'assets': assets} |

### get_heatmap_engine

Returns cached/new heatmap instance; UI/research route, not trader causal features.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [72](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:72) | Return | No enclosing if; see source try/loop/call context | HEATMAP_ENGINES[key] |

### get_live_analytics

Initial analytics load blocks; cached stale result returned while daemon refresh starts. Check/add coordination and cold initialization are not guarded per coin.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [291](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:291) | Return | not cached | LIVE_ANALYTICS_CACHE.get(coin, {}) |
| [299](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:299) | Return | No enclosing if; see source try/loop/call context | cached |

### get_universe

Refresh error retains prior nonempty universe; error on initial empty cache propagates. Global client/cache lacks synchronized multi-request refresh.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [60](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:60) | ExceptHandler | not CACHED_UNIVERSE or now - LAST_UNIVERSE_TIME > 60.0 | Exception |
| [62](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:62) | Raise | not CACHED_UNIVERSE or now - LAST_UNIVERSE_TIME > 60.0 AND not CACHED_UNIVERSE | e |
| [63](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:63) | Return | No enclosing if; see source try/loop/call context | CACHED_UNIVERSE |

### index_page

Returns dashboard HTML, no quantitative admission or order effect.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [2697](C:/Users/SIGMA/Documents/Trading_2/Terminal/Chrome_Terminal.py:2697) | Return | No enclosing if; see source try/loop/call context | HTML_TEMPLATE |

## Terminal/Cognitive_Engine.py

### CognitiveEngine._retrieve_memory

Absent ledger returns empty; parse/record errors skipped, outer IO failure yields accumulated/empty memory. Scans whole file while retaining last 2000 lines, then last three same-asset records before as_of. Duplicate decision/outcome records can bias recent context.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [151](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:151) | Return | not self.decision_ledger_path.exists() | [] |
| [172](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:172) | ExceptHandler | No enclosing if; see source try/loop/call context | ExceptHandler |
| [174](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:174) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [177](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:177) | Return | No enclosing if; see source try/loop/call context | memory |

### CognitiveEngine.build_snapshot

Returns structured candidate snapshot; legacy flow/regime fields default to zero/UNKNOWN despite richer econometrics, and historical bands are supplied alongside true projected exposures. No broker authority.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [146](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:146) | Return | No enclosing if; see source try/loop/call context | snapshot |

### CognitiveEngine.evaluate_snapshot

Network/non200/decode/schema/ledger errors return None; validated SELECT/HOLD is journaled and returned. Late successful decisions can be recorded after trader abstained. Inference default gates entry; worker never places order.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [209](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:209) | Return | resp.status_code == 200 AND not self.validate_decision(snapshot, decision) | None |
| [211](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:211) | Return | resp.status_code == 200 | decision |
| [214](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:214) | Return | NOT(resp.status_code == 200) | None |
| [215](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:215) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [217](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:217) | Return | No enclosing if; see source try/loop/call context | None |

### CognitiveEngine.validate_decision

Schema/candidate/reference/type/length failures return False. Valid references prove pointer existence, not economic interpretation; SELECT requires evidence/invalidation references. Returns boolean only.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [231](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:231) | Return | not isinstance(decision, dict) or set(decision) != set(DECISION_SCHEMA['required']) | False |
| [232](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:232) | Return | decision['snapshot_id'] != snapshot['snapshot_id'] or decision['action'] not in ('SELECT', 'HOLD') | False |
| [234](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:234) | Return | decision['action'] == 'SELECT' and decision['candidate_id'] != candidate_id | False |
| [235](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:235) | Return | decision['action'] == 'HOLD' and decision['candidate_id'] is not None | False |
| [237](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:237) | Return | not isinstance(decision[key], str) or len(decision[key]) > limit | False |
| [238](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:238) | Return | decision['abstain_reason'] is not None and (not isinstance(decision['abstain_reason'], str)) | False |
| [241](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:241) | Return | not isinstance(refs, list) or len(refs) > limit | False |
| [243](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:243) | Return | not isinstance(pointer, str) or not pointer.startswith('/') | False |
| [249](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:249) | ExceptHandler | No enclosing if; see source try/loop/call context | (KeyError, ValueError, IndexError, TypeError) |
| [249](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:249) | Return | No enclosing if; see source try/loop/call context | False |
| [250](C:/Users/SIGMA/Documents/Trading_2/Terminal/Cognitive_Engine.py:250) | Return | No enclosing if; see source try/loop/call context | decision['action'] != 'SELECT' or bool(decision['support_refs'] and decision['invalidation_refs']) |

## Terminal/Export_MT5_Ticks.py

### export_ticks

Connection/history errors raise; incomplete future episodes skipped. Returns export counts and hashes after hourly UTC quote archive. Overlapping chunks need deduplication; downstream labels do not verify this manifest.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [15](C:/Users/SIGMA/Documents/Trading_2/Terminal/Export_MT5_Ticks.py:15) | Raise | not bridge.ensure_connected() | RuntimeError('MT5 tick history unavailable') |
| [29](C:/Users/SIGMA/Documents/Trading_2/Terminal/Export_MT5_Ticks.py:29) | Raise | raw is None | RuntimeError(f'Tick history read failed for {symbol}: {mt5.last_error()}') |
| [40](C:/Users/SIGMA/Documents/Trading_2/Terminal/Export_MT5_Ticks.py:40) | Return | No enclosing if; see source try/loop/call context | {'chunks': len(manifest), 'rows': sum((m['rows'] for m in manifest)), 'output': str(output)} |

## Terminal/MT5_Execution_Bridge.py

### <module>

Missing MetaTrader5 import records module unavailable; construction subsequently tries connection. Importing this module alone does not send orders.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [25](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:25) | ExceptHandler | No enclosing if; see source try/loop/call context | ImportError |

### MT5ExecutionBridge._floor_volume

Delegates to Decimal downward volume normalization; no orders.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [207](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:207) | Return | No enclosing if; see source try/loop/call context | floor_volume(volume, step, minimum, maximum) |

### MT5ExecutionBridge.cancel_pending_order

Connection/rejected/None result returns failure; DONE returns success. Repeated inventory is needed to establish absence after ambiguous cancellation.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [550](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:550) | Return | not self.ensure_connected() | {'success': False, 'error': 'MT5 not connected'} |
| [553](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:553) | Return | result is None or result.retcode != getattr(mt5, 'TRADE_RETCODE_DONE', 10009) | {'success': False, 'retcode': getattr(result, 'retcode', None), 'error': getattr(result, 'comment', str(mt5.last_error()))} |
| [554](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:554) | Return | No enclosing if; see source try/loop/call context | {'success': True, 'ticket': int(order_ticket), 'retcode': result.retcode} |

### MT5ExecutionBridge.close_position

Connection/missing position/metadata failure returns failure. Sends full remaining volume with deviation 25; only INVALID_FILL retries FOK. None/timeout/connection is uncertain; DONE/PARTIAL returns success. Caller close flag prevents recovery of uncertain remainder.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [561](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:561) | Return | not self.ensure_connected() | {'success': False, 'error': 'MT5 not connected'} |
| [565](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:565) | Return | not positions or len(positions) == 0 | {'success': False, 'error': f'Position ticket {ticket} not found'} |
| [572](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:572) | Return | not sym_info or not tick | {'success': False, 'error': f'Tick info missing for {symbol}'} |
| [599](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:599) | Return | result is None or result.retcode not in {mt5.TRADE_RETCODE_DONE, getattr(mt5, 'TRADE_RETCODE_DONE_PARTIAL', 10010)} | {'success': False, 'uncertain': result is None or retcode in (10012, 10031), 'error': f'Close failed: {retcode} ({err})'} |
| [602](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:602) | Return | No enclosing if; see source try/loop/call context | {'success': True, 'partial': result.retcode != mt5.TRADE_RETCODE_DONE, 'ticket': ticket, 'price': result.price, 'deal': result.deal} |

### MT5ExecutionBridge.ensure_connected

Missing module/initialization/account mismatch returns False. Calls native initialization when disconnected; no account login selection or terminal-path pinning.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [48](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:48) | Return | not MT5_AVAILABLE | False |
| [55](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:55) | Return | not mt5.terminal_info() or not mt5.terminal_info().connected AND not ok | False |
| [66](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:66) | Return | self.account_id is not None AND actual != self.account_id | False |
| [67](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:67) | Return | No enclosing if; see source try/loop/call context | True |

### MT5ExecutionBridge.estimate_order

Disconnected/unusable profit or margin raises; native one-lot stop loss and margin returned. Full-volume nonlinearity is not modeled here.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [246](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:246) | Raise | not self.ensure_connected() | ValueError('Broker valuation unavailable') |
| [251](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:251) | Raise | profit is None or margin is None or profit >= 0 or (margin <= 0) | ValueError(f'Broker risk/margin calculation failed: {mt5.last_error()}') |
| [252](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:252) | Return | No enclosing if; see source try/loop/call context | {'stop_loss_per_lot': abs(float(profit)), 'margin_per_lot': float(margin)} |

### MT5ExecutionBridge.execute_market_order

Preflight connection/symbol/quote/side/spread/raw age/lot/bracket/check failures return rejection without send. Only INVALID_FILL loops filling policies. None/timeout/connection/placed after send is uncertain; DONE/PARTIAL returns actual result. Candidate reference-R drift is absent at this boundary.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [385](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:385) | Return | not self.ensure_connected() | {'success': False, 'error': 'MT5 not connected'} |
| [388](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:388) | Return | not mt5.symbol_select(symbol, True) | {'success': False, 'error': f'Symbol {symbol} select failed'} |
| [393](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:393) | Return | not sym_info or not tick | {'success': False, 'error': f'Failed to get tick for {symbol}'} |
| [397](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:397) | Return | side not in {'LONG', 'SHORT', 'BUY', 'SELL'} | {'success': False, 'error': f'Unsupported direction: {direction}'} |
| [405](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:405) | Return | max_spread_points is not None and spread_points > float(max_spread_points) | {'success': False, 'error': f'Spread guard: {spread_points:.1f} > {max_spread_points} points', 'spread_points': spread_points} |
| [410](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:410) | Return | max_tick_age_ms > 0 AND not tick_time_msc or not 0 <= age_ms <= max_tick_age_ms | {'success': False, 'error': f'Stale quote: {age_ms} ms', 'age_ms': age_ms} |
| [414](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:414) | Return | clamped_vol <= 0.0 | {'success': False, 'error': 'Requested volume is below broker minimum after risk-preserving normalization'} |
| [418](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:418) | Return | not 0 < tick.bid < tick.ask or rounded_sl <= 0 or rounded_tp <= 0 | {'success': False, 'error': 'Valid two-sided quote and protective bracket required'} |
| [420](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:420) | Return | not (rounded_sl < price < rounded_tp if is_long else rounded_tp < price < rounded_sl) | {'success': False, 'error': 'Invalid bracket direction'} |
| [450](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:450) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [451](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:451) | Return | No enclosing if; see source try/loop/call context | {'success': False, 'error': f'order_check failed: {exc}'} |
| [452](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:452) | Return | checked is None | {'success': False, 'error': 'order_check returned no result'} |
| [455](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:455) | Return | checked.retcode not in (0, getattr(mt5, 'TRADE_RETCODE_DONE', 10009)) | {'success': False, 'retcode': checked.retcode, 'error': f'order_check rejected: {checked.comment}'} |
| [466](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:466) | Return | result is None or result.retcode not in filled_codes | {'success': False, 'uncertain': uncertain, 'retcode': retcode, 'error': f'Order rejected: {retcode} ({comment_err})', 'spread_points': spread_points} |
| [469](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:469) | Return | No enclosing if; see source try/loop/call context | {'success': True, 'ticket': result.order, 'deal': result.deal, 'symbol': symbol, 'direction': direction, 'volume': float(getattr(result, 'volume', clamped_vol)), 'price': result.price, 'sl': rounded_sl, 'tp': rounded_tp, 'partial': result.retcode == getattr(mt5, 'TRADE_RETCODE_DONE_PARTIAL', 10010), 'retcode': result.retcode, 'spread_poin … (full expression in JSON) |

### MT5ExecutionBridge.get_account_summary

Connection/account failures return connected=False; valid rounded USD-labelled account fields are returned, with actual currency checked upstream.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [71](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:71) | Return | not self.ensure_connected() | {'connected': False, 'error': 'MT5 not connected'} |
| [75](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:75) | Return | not acc | {'connected': False, 'error': f'Failed to get account info: {mt5.last_error()}'} |
| [77](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:77) | Return | No enclosing if; see source try/loop/call context | {'connected': True, 'login': acc.login, 'trade_mode': acc.trade_mode, 'company': acc.company, 'currency': acc.currency, 'balance_usd': round(acc.balance, 2), 'equity_usd': round(acc.equity, 2), 'profit_usd': round(acc.profit, 2), 'margin_usd': round(acc.margin, 2), 'margin_free_usd': round(acc.margin_free, 2), 'margin_level_pct': round(ac … (full expression in JSON) |

### MT5ExecutionBridge.get_execution_quality

Missing quote returns None; valid quote yields spread metrics. Does not independently validate timestamp or execution mode.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [188](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:188) | Return | not quote | None |
| [193](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:193) | Return | No enclosing if; see source try/loop/call context | {'bid': bid, 'ask': ask, 'mid': mid, 'spread_price': spread_price, 'spread_points': spread_price / point, 'spread_bps': spread_price / mid * 10000.0 if mid > 0.0 else 0.0, 'point': point, 'digits': float(quote.get('digits', 2))} |

### MT5ExecutionBridge.get_open_positions

Disconnected or None inventory raises instead of implying no positions; valid global list returns broker identifiers and brackets.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [211](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:211) | Raise | not self.ensure_connected() | RuntimeError('Position inventory unavailable: MT5 disconnected') |
| [215](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:215) | Raise | raw_positions is None | RuntimeError(f'Position inventory failed: {mt5.last_error()}') |
| [235](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:235) | Return | No enclosing if; see source try/loop/call context | out |

### MT5ExecutionBridge.get_pending_orders

Disconnected/None raises; valid global pending list returned. Pending orders globally block new candidate entries.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [238](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:238) | Raise | not self.ensure_connected() | RuntimeError('Pending inventory unavailable') |
| [240](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:240) | Raise | orders is None | RuntimeError(f'Pending inventory failed: {mt5.last_error()}') |
| [241](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:241) | Return | No enclosing if; see source try/loop/call context | [{'ticket': o.ticket, 'symbol': o.symbol, 'magic': o.magic, 'comment': o.comment, 'volume': o.volume_current, 'expiration': o.time_expiration} for o in orders] |

### MT5ExecutionBridge.get_recent_bars

Unavailable API/timeframe/select/exception/None returns empty history. Otherwise completed bars from position one returned with unadjusted timestamp. Empty history causes downstream statistics/refit veto.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [154](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:154) | Return | not self.ensure_connected() or not hasattr(mt5, 'copy_rates_from_pos') | [] |
| [158](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:158) | Return | timeframe is None or not mt5.symbol_select(symbol, True) | [] |
| [161](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:161) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [163](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:163) | Return | No enclosing if; see source try/loop/call context | [] |
| [165](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:165) | Return | raw is None | [] |
| [182](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:182) | Return | No enclosing if; see source try/loop/call context | bars |

### MT5ExecutionBridge.get_recent_bars.value

Per-row field failures return default zero; downstream positive-close/statistics checks catch many but not all malformed metadata.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [171](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:171) | Return | No enclosing if; see source try/loop/call context | float(item) |
| [172](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:172) | ExceptHandler | No enclosing if; see source try/loop/call context | (KeyError, TypeError, ValueError, AttributeError) |
| [173](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:173) | Return | No enclosing if; see source try/loop/call context | default |

### MT5ExecutionBridge.get_symbol_price

Connection/select/missing tick/info returns None. Valid dictionary rewrites raw time through nearest-hour inference; this is the clock inconsistency.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [115](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:115) | Return | not self.ensure_connected() | None |
| [119](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:119) | Return | not mt5.symbol_select(symbol, True) | None |
| [124](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:124) | Return | not tick or not info | None |
| [126](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:126) | Return | No enclosing if; see source try/loop/call context | {'symbol': symbol, 'bid': tick.bid, 'ask': tick.ask, 'last': tick.last if tick.last > 0 else (tick.bid + tick.ask) / 2.0, 'spread': info.spread, 'point': info.point, 'digits': info.digits, 'contract_size': info.trade_contract_size, 'min_lot': info.volume_min, 'max_lot': info.volume_max, 'step_lot': info.volume_step, 'time_msc': int(getatt … (full expression in JSON) |

### MT5ExecutionBridge.modify_position_sltp

Connection/inventory/metadata/SL removal/retreat/raw-age/distance failures return success=False before send. Unknown send result returns failure; DONE returns success. Existing bracket survives ordinary rejections; successful modification is not re-queried immediately.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [290](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:290) | Return | not self.ensure_connected() | {'success': False, 'error': 'MT5 not connected'} |
| [295](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:295) | Return | not positions or len(positions) == 0 | {'success': False, 'error': f'Position ticket {ticket} not found'} |
| [302](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:302) | Return | not info or not tick | {'success': False, 'error': f'Quote metadata missing for {symbol}'} |
| [306](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:306) | Return | rounded_sl <= 0 | {'success': False, 'error': 'Protective SL cannot be removed'} |
| [309](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:309) | Return | rounded_sl > 0.0 and current_sl > 0.0 AND pos.type == mt5.ORDER_TYPE_BUY and rounded_sl < current_sl | {'success': False, 'error': 'SL ratchet cannot move a buy stop lower'} |
| [311](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:311) | Return | rounded_sl > 0.0 and current_sl > 0.0 AND pos.type == mt5.ORDER_TYPE_SELL and rounded_sl > current_sl | {'success': False, 'error': 'SL ratchet cannot move a sell stop higher'} |
| [322](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:322) | Return | not 0 <= tick_age <= 2000 or not 0 < bid < ask | {'success': False, 'error': 'Stale or invalid ratchet quote'} |
| [326](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:326) | Return | rounded_sl > 0.0 and min_distance > 0.0 AND pos.type == mt5.ORDER_TYPE_BUY and rounded_sl > bid - min_distance | {'success': False, 'error': 'SL violates buy stop/freeze distance'} |
| [328](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:328) | Return | rounded_sl > 0.0 and min_distance > 0.0 AND pos.type == mt5.ORDER_TYPE_SELL and rounded_sl < ask + min_distance | {'success': False, 'error': 'SL violates sell stop/freeze distance'} |
| [331](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:331) | Return | rounded_tp > 0.0 and min_distance > 0.0 AND pos.type == mt5.ORDER_TYPE_BUY and rounded_tp < ask + min_distance | {'success': False, 'error': 'TP violates buy stop/freeze distance'} |
| [333](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:333) | Return | rounded_tp > 0.0 and min_distance > 0.0 AND pos.type == mt5.ORDER_TYPE_SELL and rounded_tp > bid - min_distance | {'success': False, 'error': 'TP violates sell stop/freeze distance'} |
| [346](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:346) | Return | result is None | {'success': False, 'error': f'order_send failed: {err}'} |
| [349](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:349) | Return | result.retcode != mt5.TRADE_RETCODE_DONE | {'success': False, 'retcode': result.retcode, 'comment': result.comment, 'error': f'Retcode: {result.retcode} ({result.comment})'} |
| [357](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:357) | Return | No enclosing if; see source try/loop/call context | {'success': True, 'ticket': ticket, 'symbol': symbol, 'sl': rounded_sl, 'tp': rounded_tp, 'retcode': result.retcode} |

### MT5ExecutionBridge.position_deals

Disconnected/None history raises; valid all-deal components returned for outcome/reconciliation.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [255](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:255) | Raise | not self.ensure_connected() | RuntimeError('Deal history unavailable') |
| [257](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:257) | Raise | deals is None | RuntimeError('Deal history failed') |
| [258](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:258) | Return | No enclosing if; see source try/loop/call context | [{'ticket': d.ticket, 'position_id': d.position_id, 'time_msc': d.time_msc, 'entry': d.entry, 'volume': d.volume, 'price': d.price, 'profit_usd': d.profit, 'commission_usd': d.commission, 'swap_usd': d.swap, 'fee_usd': getattr(d, 'fee', 0)} for d in deals] |

### MT5ExecutionBridge.reconcile_intent_history

No matching entry returns None; ambiguous identifiers/history failure raise. Fully offset entry/exit volume returns FILLED_CLOSED; still-open or absent history remains unresolved. Exact comment matching is fragile.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [265](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:265) | Raise | not self.ensure_connected() | RuntimeError('Intent history unavailable') |
| [269](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:269) | Raise | deals is None | RuntimeError('Intent deal-history query failed') |
| [271](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:271) | Return | not entries | None |
| [273](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:273) | Raise | len(ids) != 1 | RuntimeError('Intent maps to multiple position identifiers') |
| [278](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:278) | Return | incoming > 0 and outgoing >= incoming - 1e-08 | {'state': 'FILLED_CLOSED', 'position_id': identifier, 'deals': history, 'net_pnl_usd': sum((d[k] for d in history for k in ('profit_usd', 'commission_usd', 'swap_usd', 'fee_usd')))} |
| [280](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:280) | Return | No enclosing if; see source try/loop/call context | None |

### MT5ExecutionBridge.resolve_symbol

Cache/exact alias hit returns symbol; connection/list/no match returns None. No fuzzy synthetic fallback; broker availability remains required.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [94](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:94) | Return | coin in self._symbol_cache | self._symbol_cache[coin] |
| [97](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:97) | Return | not self.ensure_connected() | None |
| [102](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:102) | Return | not symbols | None |
| [108](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:108) | Return | name in candidates | name |
| [111](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:111) | Return | No enclosing if; see source try/loop/call context | None |

### MT5ExecutionBridge.stage_limit_order

Dormant in OMNI market-only CLI. Rejects connection/side/select/quote/spread/nonpositive/passivity/min-lot failures; sends pending order without equivalent order_check/freshness/protective-bracket rigor. None send is not labelled uncertain. Do not enable without a separately validated policy.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [500](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:500) | Return | not self.ensure_connected() | {'success': False, 'error': 'MT5 not connected'} |
| [503](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:503) | Return | side not in {'LONG', 'SHORT', 'BUY', 'SELL'} | {'success': False, 'error': f'Unsupported direction: {direction}'} |
| [506](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:506) | Return | not mt5.symbol_select(symbol, True) | {'success': False, 'error': f'Symbol {symbol} select failed'} |
| [509](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:509) | Return | not info or not tick | {'success': False, 'error': f'Quote metadata missing for {symbol}'} |
| [513](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:513) | Return | max_spread_points is not None and spread_points > float(max_spread_points) | {'success': False, 'error': f'Spread guard: {spread_points:.1f} > {max_spread_points} points'} |
| [516](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:516) | Return | price <= 0.0 | {'success': False, 'error': 'Limit price must be positive'} |
| [518](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:518) | Return | passive_only and (not (float(tick.bid) <= price < float(tick.ask) if is_long else float(tick.bid) < price <= float(tick.ask))) | {'success': False, 'error': 'Limit is not passive and was rejected by passive_only guard'} |
| [521](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:521) | Return | normalized <= 0.0 | {'success': False, 'error': 'Requested volume is below broker minimum'} |
| [543](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:543) | Return | result is None or result.retcode not in placed_codes | {'success': False, 'retcode': retcode, 'error': f'Limit order rejected: {retcode} ({error})'} |
| [545](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:545) | Return | No enclosing if; see source try/loop/call context | {'success': True, 'ticket': getattr(result, 'order', 0), 'symbol': symbol, 'direction': direction, 'volume': normalized, 'price': price, 'sl': request['sl'], 'tp': request['tp'], 'expires_at': request['expiration'], 'spread_points': spread_points} |

## Terminal/Macro_Calendar.py

### download

HTTP/decode errors propagate; socket timeout is not verified complete coverage.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [17](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:17) | Return | No enclosing if; see source try/loop/call context | response.read().decode('utf-8') |

### parse_bls

Missing timestamp/unusable event coverage raises; dated CPI/NFP events use UTC or Eastern ZoneInfo, including DST.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [31](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:31) | Raise | len(stamps) != 1 | ValueError('BLS event lacks DTSTART') |
| [40](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:40) | Raise | not events | ValueError('BLS calendar format changed or has no CPI/NFP dates') |
| [41](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:41) | Return | No enclosing if; see source try/loop/call context | events |

### parse_fed

Missing/changed section or date/time raises; otherwise dated FOMC/minutes/conference entries returned. Empty valid section can represent a no-meeting month but needs independent coverage attestation.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [47](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:47) | Raise | len(headings) != 1 | ValueError('Fed calendar format changed: FOMC section missing') |
| [59](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:59) | Raise | not match or not days | ValueError('Fed event time/date unparseable') |
| [65](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:65) | Return | No enclosing if; see source try/loop/call context | events |

### refresh_calendar

Requires CPI/NFP current-month coverage; optional following month failure truncates coverage after current successful month. Failure before publish preserves prior file. Whole-calendar temp replacement is atomic but unsigned declaration is trusted by reader.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [79](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:79) | Raise | not {'CPI', 'NFP'}.issubset({e['name'] for e in releases}) | ValueError('BLS calendar lacks complete current-month CPI/NFP coverage') |
| [82](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:82) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [84](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:84) | Raise | No enclosing if; see source try/loop/call context | Raise |
| [92](C:/Users/SIGMA/Documents/Trading_2/Terminal/Macro_Calendar.py:92) | Return | No enclosing if; see source try/loop/call context | result |

## Terminal/Market_Intelligence.py

### MarketIntelligenceEngine._compute_sentiment_score

No headlines returns after resetting zero; otherwise substring keyword counts set bounded global score. Negation/deduplication/source reliability are not modeled.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [111](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:111) | Return | not self.cached_headlines | Return |

### MarketIntelligenceEngine.asset_sentiment_scores

Invalid/future/old publication timestamps skip headlines. Substring asset/macro relevance and half-life weights create bounded per-asset scores. Generic macro direction is applied identically to all assets, without rate/FX transmission modeling.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [204](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:204) | ExceptHandler | No enclosing if; see source try/loop/call context | (ValueError, TypeError, KeyError) |
| [215](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:215) | Return | No enclosing if; see source try/loop/call context | scores |

### MarketIntelligenceEngine.check_macro_blackout

Invalid/missing/out-of-coverage calendar normally returns active CALENDAR_UNAVAILABLE; HIGH event within inclusive window returns active event. Otherwise NO_EVENT; empty events and absent verified_at can falsely pass.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [143](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:143) | Raise | calendar.get('required_series') != ['CPI', 'NFP', 'FOMC'] | ValueError('calendar coverage unverified') |
| [145](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:145) | Raise | not epoch(calendar.get('coverage_start')) <= now < epoch(calendar.get('coverage_end')) | ValueError('calendar outside verified coverage') |
| [146](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:146) | Raise | epoch(calendar.get('verified_at')) > now | ValueError('future calendar vintage') |
| [152](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:152) | Raise | not event_time | ValueError('calendar event timestamp invalid') |
| [154](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:154) | Return | delta <= self.blackout_minutes | (True, event['name'], delta) |
| [155](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:155) | Return | No enclosing if; see source try/loop/call context | (False, 'NO_EVENT', 999.0) |
| [156](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:156) | ExceptHandler | No enclosing if; see source try/loop/call context | (OSError, ValueError, KeyError, TypeError) |
| [158](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:158) | Return | No enclosing if; see source try/loop/call context | (True, 'CALENDAR_UNAVAILABLE', 0.0) |

### MarketIntelligenceEngine.fetch_live_headlines

Fresh nonempty cache returns early; individual feed errors skip feed. Successful fetch updates cache/sentiment; all failures retain old cache. Publication dates are applied in asset scoring, not transport freshness.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [71](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:71) | Return | self.cached_headlines and now - self.last_fetch_time < 300.0 | self.cached_headlines |
| [95](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:95) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |
| [103](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:103) | Return | No enclosing if; see source try/loop/call context | self.cached_headlines |

### MarketIntelligenceEngine.get_market_intelligence_report

Calendar refresh failure warns and preserves prior calendar; report returns sentiment/date/blackout health. Macro worker reception time is assigned separately by trader and can extend cached report apparent age.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [168](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:168) | ExceptHandler | self.clock() - self.last_calendar_attempt > 86400 | Exception |
| [177](C:/Users/SIGMA/Documents/Trading_2/Terminal/Market_Intelligence.py:177) | Return | No enclosing if; see source try/loop/call context | {'timestamp_utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'), 'macro_sentiment_score': self.cached_sentiment, 'asset_scores': self.asset_sentiment_scores(), 'sentiment_valid': bool(self.cached_headlines and self.clock() - self.last_fetch_time <= 900), 'calendar_error': self.calendar_error, 'macro_bias': … (full expression in JSON) |

## Terminal/Microstructure.py

### TokenBucket.acquire

Locked refill permits return when token available; otherwise sleeps outside lock. No cyclic lock hold, but request starvation/deadline overrun is possible without a caller timeout.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [51](C:/Users/SIGMA/Documents/Trading_2/Terminal/Microstructure.py:51) | Return | self.tokens >= 1 | Return |

### classify_liquidation

Explicit side returns canonical direction; otherwise price-location heuristic. This is not authoritative liquidation semantics and must remain labelled as fallback.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [24](C:/Users/SIGMA/Documents/Trading_2/Terminal/Microstructure.py:24) | Return | side AND s in {'LONG', 'BUY', 'B'} | 'LONG' |
| [25](C:/Users/SIGMA/Documents/Trading_2/Terminal/Microstructure.py:25) | Return | side AND s in {'SHORT', 'SELL', 'A'} | 'SHORT' |
| [26](C:/Users/SIGMA/Documents/Trading_2/Terminal/Microstructure.py:26) | Return | No enclosing if; see source try/loop/call context | 'LONG' if price < current_price else 'SHORT' |

### safe_imbalance

Returns bounded imbalance of nonnegative sides or zero for absent total; zero conflates no measured flow with balanced flow.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [31](C:/Users/SIGMA/Documents/Trading_2/Terminal/Microstructure.py:31) | Return | No enclosing if; see source try/loop/call context | (positive - negative) / total if total > 0 else 0.0 |

## Terminal/OF_Strategy.py

### main

CLI validates mode, selects legacy research/inspection or constructs the trader. Paper is default. Inspection can report errors with successful process exit. Optional account/sigma/cognition flags affect the actual live contract.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [52](C:/Users/SIGMA/Documents/Trading_2/Terminal/OF_Strategy.py:52) | Return | args.mode == 'backtest' | Return |
| [62](C:/Users/SIGMA/Documents/Trading_2/Terminal/OF_Strategy.py:62) | ExceptHandler | args.mode == 'inspect' | Exception |
| [67](C:/Users/SIGMA/Documents/Trading_2/Terminal/OF_Strategy.py:67) | Return | args.mode == 'inspect' | Return |

## Terminal/Omni_Trader.py

### AI15mMT5Trader.__init__

Invalid cadence/universe/entry mode raises. State parse/type and native artifact errors can be fatal before run; selected covariance loader errors fall back to another artifact. Workers do not send orders.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [34](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:34) | Raise | cadence_minute != 14 or not 0 <= cadence_second <= 50 | ValueError('Entries must be scheduled in minute 14 before the candle close') |
| [36](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:36) | Raise | entry_mode != 'market' | ValueError('OMNI uses market execution; pending limit routing requires a separately validated fill policy') |
| [40](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:40) | Raise | any((a not in UNIVERSE for a in self.assets)) or len(set(self.assets)) != len(self.assets) | ValueError('Invalid asset allow-list') |
| [77](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:77) | ExceptHandler | self.covariance is None | (OSError, ValueError, KeyError) |

### AI15mMT5Trader._account

Disconnected/non-USD/unknown identity and persisted mismatch raise. Paper valuation uses executable quotes, contract arithmetic and residual modeled costs. Live account equity is not adjusted for reserved exit costs.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [162](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:162) | Raise | not account.get('connected') or account.get('currency') != 'USD' | ValueError('USD_broker_account_required') |
| [165](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:165) | Raise | not self.paper_mode AND not login | ValueError('broker_account_identity_unavailable') |
| [166](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:166) | Raise | not self.paper_mode AND self.state.get('account_login') not in (None, login) | ValueError('persisted_state_account_mismatch') |
| [175](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:175) | Return | No enclosing if; see source try/loop/call context | account |

### AI15mMT5Trader._close

Early return for any close_uncertain flag suppresses all future close attempts. Live preparation persists before RPC; exception or uncertain result can leave flag permanently set. Paper closes update cash and log outcomes.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [242](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:242) | Return | metadata.get('close_uncertain') | Return |

### AI15mMT5Trader._dispatch

Unique persisted intent precedes live RPC. Any send exception becomes UNCERTAIN. Explicit success/uncertain/rejection selects intent status; no blind same-slot resend. Journal/disk errors outside send handler may interrupt result persistence.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [503](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:503) | Raise | key in self.state['intents'] | ValueError('duplicate_execution_intent') |
| [521](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:521) | ExceptHandler | NOT(self.paper_mode) | Exception |
| [526](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:526) | Return | No enclosing if; see source try/loop/call context | result |

### AI15mMT5Trader._equity_guard

Returns guard and mutates peak/latch. Uses mutable persisted capital; no immutable-capital validation or controlled reset.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [184](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:184) | Return | No enclosing if; see source try/loop/call context | {'equity_usd': equity, 'peak_equity_usd': peak, 'hard_floor_usd': floor, 'drawdown_room': max(0, equity - floor), 'halted': self.state['halted']} |

### AI15mMT5Trader._fetch

HTTP, decode and identity failures escape to the completed-future handler; response body has no complete schema or byte bound.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [100](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:100) | Raise | canonical_asset(payload.get('coin')) != asset | ValueError('Signal asset mismatch') |
| [101](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:101) | Return | No enclosing if; see source try/loop/call context | payload |

### AI15mMT5Trader._inventory

Real inventory/pending read errors raise even in paper. Paper returns simulated inventory and no pending orders; live returns actual global inventory.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [157](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:157) | Return | self.paper_mode | (copy.deepcopy(self.state['paper_positions']), []) |
| [158](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:158) | Return | No enclosing if; see source try/loop/call context | (actual, pending) |

### AI15mMT5Trader._own

Boolean magic/ticket ownership test; foreign positions are counted elsewhere but not managed or flattened here.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [151](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:151) | Return | No enclosing if; see source try/loop/call context | int(position.get('magic', 0)) == MAGIC or str(position.get('ticket')) in self.state['positions'] |

### AI15mMT5Trader._portfolio_exposure

Missing SL/initial R/quotes/coverage raise and stop candidate sizing. Returns signed notional, remaining drawdown room and first-position features using linear contract arithmetic.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [319](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:319) | Raise | number(p.get('sl')) <= 0 | ValueError('portfolio_has_unprotected_position') |
| [324](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:324) | Raise | initial_r <= 0 | ValueError('portfolio_initial_r_unknown') |
| [330](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:330) | Return | No enclosing if; see source try/loop/call context | (exposure, max(0, guard['drawdown_room'] - stop_reserve), enriched) |

### AI15mMT5Trader._quote

Invalid sides or strategy-clock freshness raise. Normalized timestamp can hide hour-old ticks. Caller determines whether this vetoes an asset, ignores capture, or aborts portfolio valuation.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [145](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:145) | Raise | not quote or not 0 < number(quote.get('bid')) < number(quote.get('ask')) | ValueError('broker_quote_invalid') |
| [148](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:148) | Raise | not -max_skew <= age <= max(5.0, getattr(self.policy, 'max_book_age', 10.0)) | ValueError('broker_quote_stale_or_future') |
| [149](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:149) | Return | No enclosing if; see source try/loop/call context | quote |

### AI15mMT5Trader._reconcile

Entry intents reconcile exact comment/magic or filled-closed history. Ambiguous/missing data holds or raises, never proves no fill. Missing SL/excessive fill risk initiates close; closed-position outcomes journal before state deletion and can duplicate after a crash.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [192](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:192) | Raise | matched AND len(matched) != 1 | ValueError('ambiguous_order_reconciliation') |

### AI15mMT5Trader.capture_quotes

Quote ValueError is silently ignored per symbol; other failures abort capture/cycle. Journals POLLED_QUOTES, not full exchange/MT5 tick history.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [538](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:538) | ExceptHandler | No enclosing if; see source try/loop/call context | ValueError |

### AI15mMT5Trader.evaluate_market

Cadence/consumed slot/initial-feed returns precede slot persistence. Global drawdown/macro/pending/max-two/intents veto. Per-asset selected exceptions veto only that asset; malformed types can escape. Selection waits for cognition by default, then quote/inventory/risk/uplift rechecks precede one dispatch. Logging/state failures can escape.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [337](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:337) | Return | not 840 + self.cadence_second <= elapsed < 898 and (not (force and self.paper_mode)) | {**report, 'reason': 'outside_execution_window'} |
| [338](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:338) | Return | self.state['last_slot'] >= slot | {**report, 'reason': 'slot_already_evaluated'} |
| [340](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:340) | Return | multi_data is None and self.fetches and any((a not in self.payloads for a in self.assets)) and (elapsed < 888) | {**report, 'reason': 'waiting_for_initial_feeds'} |
| [364](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:364) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND self.covariance is None | ValueError('covariance_unavailable:' + str(self.covariance_error)) |
| [375](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:375) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND features['confluence'] < self.policy.min_confluence | ValueError('confluence_below_threshold') |
| [379](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:379) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND abs(math.log(mid / features['signal_mid'])) / features['sigma_h'] > self.policy.max_basis_sigma | ValueError('signal_broker_basis_dislocation') |
| [391](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:391) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND not sizing['accepted'] | ValueError(sizing['reason']) |
| [393](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:393) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND target_r - friction_r < 1.5 | ValueError('net_payoff_insufficient_after_friction') |
| [395](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:395) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND self.max_spread_points is not None and (quote['ask'] - quote['bid']) / quote['point'] > self.max_spread_points | ValueError('spread_limit') |
| [397](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:397) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND quote.get('currency_profit') not in (None, 'USD') | ValueError('non_USD_profit_currency_unsupported') |
| [419](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:419) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND enriched AND not gate['accepted'] | ValueError(gate['reason']) |
| [422](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:422) | ExceptHandler | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) | (ValueError, KeyError, RuntimeError) |
| [449](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:449) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND candidates AND self.cognitive_enabled AND not decision or decision.get('action') != 'SELECT' | ValueError('cognitive_abstention') |
| [451](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:451) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND candidates AND self.clock() >= deadline and (not (force and self.paper_mode)) | ValueError('execution_deadline_elapsed') |
| [456](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:456) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND candidates AND abs(px - best['price_open']) > 0.05 * best['initial_r'] | ValueError('price_moved_during_inference') |
| [457](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:457) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND candidates AND self.clock() - best['features']['book_as_of'] > self.policy.max_book_age | ValueError('book_expired_during_inference') |
| [460](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:460) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND candidates AND refreshed_pending or len(refreshed_positions) != len(positions) or {p['ticket'] for p in refreshed_positions} != {p['ticket … (full expression in JSON) | ValueError('portfolio_changed_during_inference') |
| [463](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:463) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND candidates AND fresh_guard['halted'] | ValueError('drawdown_during_inference') |
| [464](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:464) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND candidates AND self.intel.check_macro_blackout()[0] | ValueError('blackout_started_during_inference') |
| [470](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:470) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND candidates AND not recheck['accepted'] | ValueError('dispatch_risk_recheck_failed') |
| [491](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:491) | Raise | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) AND candidates AND refreshed_positions AND not gate['accepted'] | ValueError('dispatch_' + gate['reason']) |
| [494](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:494) | ExceptHandler | NOT(guard['halted']) AND NOT(blackout) AND NOT(pending) AND NOT(len(positions) >= 2) AND NOT(any((i['status'] in ('PREPARED', 'ACKNOWLEDGED', 'UNCERTAIN') for i in self.state['intents'].values()))) | (ValueError, RuntimeError, KeyError) |
| [498](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:498) | Return | No enclosing if; see source try/loop/call context | report |

### AI15mMT5Trader.manage_active_positions

Latched drawdown saves and flattens owned inventory then returns before reconciliation. Per-position valuation/ratchet errors are collected only for selected types. Unknown R keeps existing protection until time limit. SL/TP/time decay branches close; valid tighter ratchets modify.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [269](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:269) | Return | guard['halted'] | [{'event': 'hard_drawdown_stop', **guard}] |
| [306](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:306) | ExceptHandler | No enclosing if; see source try/loop/call context | (ValueError, RuntimeError) |
| [309](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:309) | Return | No enclosing if; see source try/loop/call context | changes |

### AI15mMT5Trader.refresh_background

Completed fetch errors are journaled and prior payload retained; successful results are published on the main thread. Macro errors retain prior report. Journal failure itself can escape. Socket inactivity timeouts do not enforce complete future deadlines.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [110](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:110) | ExceptHandler | future.done() | Exception |
| [118](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:118) | ExceptHandler | self.macro_future and self.macro_future.done() | Exception |

### AI15mMT5Trader.refresh_broker_history

Early return before 900 seconds; valid covering covariance is retained. Refit errors of selected types are recorded, but symbol/history reads before the try and native library errors can abort the cycle.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [126](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:126) | Return | now - self.last_bars < 900 | Return |
| [136](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:136) | Return | self.covariance AND all((a in self.covariance.index for a in self.bars)) | Return |
| [140](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:140) | ExceptHandler | No enclosing if; see source try/loop/call context | (ValueError, OSError, ImportError) |

### AI15mMT5Trader.run

Byte lock rejection stops competing same-mode writer. Main-cycle exceptions are logged then loop resumes; logger failure can escape. Finally saves before cleanup, so failed state write can skip explicit shutdown/unlock. No built-in reboot supervisor.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [549](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:549) | ExceptHandler | No enclosing if; see source try/loop/call context | OSError |
| [550](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:550) | Raise | No enclosing if; see source try/loop/call context | RuntimeError('Another OMNI writer owns this execution mode') |
| [561](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:561) | ExceptHandler | No enclosing if; see source try/loop/call context | Exception |

## Terminal/Risk_Sizing_Engine.py

### CovarianceGate.__init__

Rejects labels/shape/nonfinite/symmetry/PSD/diagonal violations. Metadata provenance is not authenticated by numeric matrix validation.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [247](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:247) | Raise | len(set(self.assets)) != n or self.matrix.shape != (n, n) or (not np.isfinite(self.matrix).all()) | ValueError('invalid_covariance_labels_or_shape') |
| [248](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:248) | Raise | not np.allclose(self.matrix, self.matrix.T, rtol=1e-05, atol=1e-12) | ValueError('asymmetric_covariance') |
| [250](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:250) | Raise | np.min(np.linalg.eigvalsh(self.matrix)) < -1e-12 or np.any(np.diag(self.matrix) <= 0) | ValueError('covariance_not_positive_semidefinite') |

### CovarianceGate.correlation

Returns normalized matrix covariance; missing labels raise KeyError. Candidate and first-position direction signs are applied by the trader.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [305](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:305) | Return | No enclosing if; see source try/loop/call context | float(self.matrix[i, j] / math.sqrt(self.matrix[i, i] * self.matrix[j, j])) |

### CovarianceGate.load

Manifest/checksum/Parquet/columns/matrix errors raise. Byte checksum cannot prove source data or estimator correctness; native Polars exceptions require explicit caller handling.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [258](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:258) | Raise | metadata.get('sha256') != hashlib.sha256(path.read_bytes()).hexdigest() | ValueError('covariance_checksum_mismatch') |
| [262](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:262) | Return | No enclosing if; see source try/loop/call context | cls(assets, df.select(assets).to_numpy(), metadata) |

### CovarianceGate.scale_candidate

Unknown coverage raises; full size is accepted if total variance fits, otherwise upper root is scaled and verified. Returns diagnostic variance and scale. Lot rounding/recheck occurs in size_trade.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [283](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:283) | Raise | key not in self.index | ValueError(f'covariance_asset_missing:{key}') |
| [287](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:287) | Raise | canonical_asset(a) not in self.index | ValueError(f'covariance_asset_missing:{a}') |
| [300](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:300) | Return | No enclosing if; see source try/loop/call context | {'scale': scale, 'variance_before': before, 'variance_after': before + A * scale ** 2 + B * scale, 'incremental_variance': A * scale ** 2 + B * scale, 'sigma_budget_usd': sigma_budget} |

### CovarianceGate.validate_time

Unknown units/horizon or future/stale times raise. Manifest controls maximum age, so a huge declared expiry passes.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [267](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:267) | Raise | meta.get('return_units') != 'decimal_log_return' or meta.get('horizon_minutes') != horizon_minutes | ValueError('covariance_units_or_horizon_unknown') |
| [269](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:269) | Raise | epoch(meta.get('created_at')) > as_of | ValueError('covariance_future_vintage') |
| [271](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:271) | Raise | not data_end or data_end > as_of or as_of - data_end > number(meta.get('max_age_seconds'), 86400) | ValueError('covariance_stale_or_future') |

### CovarianceGate.variance

Unknown asset raises; signed exposures accumulate, nonfinite values may coerce to zero through number. Returns nonnegative quadratic result.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [277](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:277) | Raise | key not in self.index | ValueError(f'covariance_asset_missing:{key}') |
| [279](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:279) | Return | No enclosing if; see source try/loop/call context | max(0.0, float(vector @ self.matrix @ vector)) |

### OrderflowModel._levels

Filters malformed-side/nonpositive numeric levels, takes first twenty, converts to USD and spatially decays. Non-dict rows raise; ordering/duplicates and instrument unit mappings are not validated.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [143](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:143) | Return | No enclosing if; see source try/loop/call context | out |

### OrderflowModel.features

Statistics/book failures raise before scoring. Malformed component types can escape asset catches. Optional missing components become zero scores; future tape accepted, partial corridors divided by visible fragment, macro denominator discontinuous. Returns bounded S/Q and requested risk, not a validated probability of profit.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [152](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:152) | Raise | not observed or not -max_future_skew <= as_of - observed <= self.policy.max_book_age | ValueError('book_stale_or_future') |
| [154](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:154) | Raise | not 0 < bid < ask | ValueError('book_crossed_or_missing') |
| [157](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:157) | Raise | not bids or not asks | ValueError('depth_missing') |
| [159](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:159) | Raise | not math.isfinite(b + a) or b + a <= 0 | ValueError('weighted_depth_invalid') |
| [233](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:233) | Return | No enclosing if; see source try/loop/call context | {**stats, 'asset': asset, 'as_of': as_of, 'signal_mid': mid, 'book_as_of': observed, 'direction': 'LONG' if direction == 1 else 'SHORT', 'l2_imbalance': imbalance, 'l2_signal': l2, 'l2_robust_z': z, 'wall_imbalance': wall_imb, 'aggressor_imbalance': tape, 'liquidation_delta': liq_delta, 'macro_score': macro_value, 'confluence': confluence … (full expression in JSON) |

### OrderflowModel.observe_walls

Invalid/out-of-order/stale source returns False; otherwise atomically replaces sampled cluster set for that asset. Missing component time falls back to response time and +10 seconds is accepted.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [118](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:118) | Return | not wall_asof or not -10.0 <= as_of - wall_asof <= 30 | False |
| [120](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:120) | Return | previous and wall_asof < max((v['last'] for v in previous.values())) | False |
| [130](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:130) | Return | No enclosing if; see source try/loop/call context | True |

### RiskPolicy.__post_init__

Rejects out-of-range trade risk and altered fixed capital/drawdown/positions. Friction lower bound and positive sigma are checked; sigma ceiling and complete finite/type validation are absent.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [55](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:55) | Raise | not 10 <= self.min_risk <= self.max_risk <= 45 | ValueError('Risk must stay inside 10 to 45 USD') |
| [57](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:57) | Raise | self.initial_capital != 5000 or self.drawdown_fraction != 0.045 or self.max_positions != 2 | ValueError('OMNI capital, drawdown and position invariants are fixed') |
| [59](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:59) | Raise | self.minimum_friction_bps < 41 or self.sigma_budget_usd <= 0 | ValueError('Invalid friction/variance budget') |

### RobustNormalizer.export

Returns in-memory normalization history; no independent file IO or order effect.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [107](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:107) | Return | No enclosing if; see source try/loop/call context | {k: list(v) for k, v in self.history.items()} |

### RobustNormalizer.score_then_observe

Returns prior-history robust z or None during warmup, then appends current value. Caller must preserve consistent observation cadence and finite stored history.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [105](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:105) | Return | No enclosing if; see source try/loop/call context | z |

### completed_statistics

History/price/staleness/contiguous returns/sigma failures raise. Forming bars excluded. ATR and ER use completed prices; session-gap returns excluded from sigma.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [72](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:72) | Raise | len(ordered) < 25 | ValueError('volatility_history_insufficient') |
| [74](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:74) | Raise | np.any(closes <= 0) | ValueError('invalid_bar_price') |
| [76](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:76) | Raise | as_of - times[-1] - 900 > 900 | ValueError('completed_bars_stale') |
| [80](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:80) | Raise | len(returns) < 24 | ValueError('continuous_return_history_insufficient') |
| [82](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:82) | Raise | not math.isfinite(sigma) or sigma <= 1e-08 | ValueError('volatility_unavailable') |
| [88](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:88) | Return | No enclosing if; see source try/loop/call context | {'sigma_h': sigma, 'atr': atr, 'efficiency_ratio': er, 'last_bar_close': float(times[-1] + 900), 'bar_count': len(ordered)} |

### cost_bps

Nonpositive mid raises; returns max(41, live spread + configured commission + slippage). This is a model reserve, not broker fee reconciliation.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [341](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:341) | Raise | mid <= 0 | ValueError('invalid_broker_quote') |
| [343](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:343) | Return | No enclosing if; see source try/loop/call context | max(policy.minimum_friction_bps, spread + policy.commission_bps + policy.slippage_bps) |

### epoch

ISO parsing treats naive times as UTC; bad ISO becomes zero. Large numeric values are interpreted as milliseconds. Unsupported timestamp conventions are not inferred safely.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [30](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:30) | Return | isinstance(value, str) and (not value.replace('.', '', 1).isdigit()) | parsed.replace(tzinfo=timezone.utc).timestamp() if parsed.tzinfo is None else parsed.timestamp() |
| [31](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:31) | ExceptHandler | isinstance(value, str) and (not value.replace('.', '', 1).isdigit()) | ValueError |
| [31](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:31) | Return | isinstance(value, str) and (not value.replace('.', '', 1).isdigit()) | 0.0 |
| [33](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:33) | Return | No enclosing if; see source try/loop/call context | value / 1000 if value > 100000000000.0 else value |

### fit_covariance

Insufficient/common/constant history raises; valid completed aligned returns produce LedoitWolf matrix and manifest. Matrix replacement and manifest write are separate publication steps.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [320](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:320) | Raise | not series | ValueError('covariance_history_unavailable') |
| [322](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:322) | Raise | len(aligned) < min_observations | ValueError('covariance_common_history_insufficient') |
| [327](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:327) | Raise | np.any(np.std(returns, axis=0) <= 1e-08) | ValueError('covariance_constant_asset_history') |
| [337](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:337) | Return | No enclosing if; see source try/loop/call context | CovarianceGate(assets, estimator.covariance_, metadata) |

### floor_volume

Invalid lot metadata returns zero; otherwise Decimal floor preserves a downward lot bound. Malformed/nonfinite inputs can still raise.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [62](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:62) | Return | step <= 0 or minimum <= 0 or maximum < minimum | 0.0 |
| [66](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:66) | Return | No enclosing if; see source try/loop/call context | float(result) if float(result) >= minimum else 0.0 |

### number

Finite numeric values pass; nonfinite/malformed values become a default. This is tolerant coercion, not source validation, and can hide invalid exposure as zero.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [21](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:21) | Return | No enclosing if; see source try/loop/call context | value if math.isfinite(value) else default |
| [22](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:22) | ExceptHandler | No enclosing if; see source try/loop/call context | (TypeError, ValueError) |
| [23](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:23) | Return | No enclosing if; see source try/loop/call context | default |

### size_trade

Missing valuation raises. Insufficient drawdown/risk or floor/covariance room returns accepted=False. Otherwise lot-floor and final risk/variance invariants precede accepted=True. Does not transmit an order.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [349](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:349) | Raise | min(notional_per_lot, stop_loss_per_lot, margin_per_lot) <= 0 | ValueError('broker_valuation_missing') |
| [353](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:353) | Return | budget < policy.min_risk | {'accepted': False, 'reason': 'drawdown_or_risk_room'} |
| [359](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:359) | Return | volume <= 0 or planned < policy.min_risk | {'accepted': False, 'reason': 'minimum_lot_or_variance_budget', **check} |
| [362](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:362) | Raise | planned > budget + 1e-08 or variance > policy.sigma_budget_usd ** 2 + 1e-08 | ValueError('sizing_invariant_failure') |
| [363](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:363) | Return | No enclosing if; see source try/loop/call context | {'accepted': True, 'volume': volume, 'risk_usd': planned, 'stop_risk_usd': volume * stop_loss_per_lot, 'friction_usd': volume * friction_per_lot, 'friction_bps': cost_bps(quote, policy), 'signed_notional_usd': sign * volume * notional_per_lot, **check, 'variance_after': variance} |

## Terminal/Uplift_Model.py

### UpliftGate.__init__

Caught filesystem/JSON/schema/checksum/import failures set unavailable status. Native LightGBMError escapes; checksum-consistent invalid models can prevent trader startup.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [217](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:217) | Raise | self.meta.get('features') != list(FEATURES) or self.meta.get('policy_version') != POLICY_VERSION | ValueError('uplift_schema_mismatch') |
| [219](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:219) | Raise | hashlib.sha256((path / name).read_bytes()).hexdigest() != self.meta['sha256'][name] | ValueError('uplift_checksum_mismatch') |
| [222](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:222) | ExceptHandler | No enclosing if; see source try/loop/call context | (OSError, ValueError, KeyError, ImportError) |

### UpliftGate.decide

Unavailable/unqualified/stale/future models return accepted=False. Valid model predicts calibrated probability and expectancy; threshold pair determines acceptance. Malformed calibration metadata/native prediction errors can raise.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [225](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:225) | Return | self.error or self.classifier is None | {'accepted': False, 'reason': 'uplift_model_unavailable', 'detail': self.error} |
| [226](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:226) | Return | not self.meta.get('live_eligible') | {'accepted': False, 'reason': 'uplift_oos_not_qualified'} |
| [230](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:230) | Return | not data_end or not created or data_end > as_of or (created > as_of) or (as_of - data_end > age_limit) or (as_of - created > age_limit) | {'accepted': False, 'reason': 'uplift_stale_or_future'} |
| [237](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:237) | Return | No enclosing if; see source try/loop/call context | {'accepted': accepted, 'reason': 'uplift_positive' if accepted else 'uplift_expectancy_veto', 'probability_positive': probability, 'expectancy_usd': expectancy, 'expectancy_buffer_usd': self.meta['expectancy_buffer_usd']} |

### executable_ratchet

Returns proposed tick-rounded stop only if distance and minimum-tightening constraints pass, else current stop. No order API.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [41](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:41) | Return | No enclosing if; see source try/loop/call context | proposed if valid and sign * (proposed - current_sl) >= tick_size * 0.99 else current_sl |

### feature_vector

Missing/nonfinite features raise before prediction; valid eighteen-column vector returned in fixed order.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [45](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:45) | Raise | not np.isfinite(values).all() | ValueError('uplift_features_missing_or_nonfinite') |
| [46](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:46) | Return | No enclosing if; see source try/loop/call context | values |

### label_episodes

Replay ValueError excludes that episode with reason; parse/native/schema errors can abort the batch. Labels are written after all episodes; no exporter-manifest hash validation.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [135](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:135) | ExceptHandler | No enclosing if; see source try/loop/call context | ValueError |
| [137](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:137) | Return | No enclosing if; see source try/loop/call context | {'labels': len(labels), 'excluded': errors} |

### ratchet

Below threshold returns current SL; staged targets tighten directionally and cannot retreat. Price R does not automatically clear friction.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [31](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:31) | Return | lock is None | current_sl |
| [33](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:33) | Return | current_sl <= 0 | proposed |
| [34](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:34) | Return | No enclosing if; see source try/loop/call context | max(current_sl, proposed) if sign == 1 else min(current_sl, proposed) |

### replay_episode

Returns paired six-hour net-equity difference after deterministic quote replay. Coverage/gaps raise; fixed floor, tick-frequency ratchets and frozen ATR diverge from live. Raw episode policy and tick authenticity are not verified.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [106](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:106) | Raise | any((counts[s] < 2 or first_seen.get(s, end) - start > 30 or end - last_seen.get(s, start) > 30 for s in required)) | ValueError('episode_quote_coverage_incomplete') |
| [110](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:110) | Raise | any((b - a > 30 for a, b in zip(times, times[1:]))) | ValueError('episode_quote_gap') |
| [120](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:120) | Return | No enclosing if; see source try/loop/call context | {'episode_id': episode['episode_id'], 'as_of': start, 'label_end': end, 'features': episode['features'], 'uplift_usd': finals[1] - finals[0], 'equity_reject': finals[0], 'equity_accept': finals[1], 'policy_version': POLICY_VERSION, 'source': 'paired_MT5_quote_replay', 'tick_quality': 'FULL_MT5_TICKS' if rows and all((t.get('feed_kind') == … (full expression in JSON) |

### train_uplift

Label count/availability/source strings/identity/horizon/purged-fold/class failures raise. Fits/calibrates on earlier folds and marks eligibility from selected test statistics and self-declared full-tick flag. Synthetic provenance can pass.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [144](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:144) | Raise | len(rows) < min_train + 120 | ValueError('Need at least 320 complete replay labels') |
| [145](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:145) | Raise | any((r['label_end'] > time.time() for r in rows)) | ValueError('Future uplift outcomes are not observable') |
| [147](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:147) | Raise | any((r.get('source') != 'paired_MT5_quote_replay' or r.get('policy_version') != POLICY_VERSION for r in rows)) | ValueError('Unverified or incompatible uplift labels') |
| [153](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:153) | Raise | not all((math.isfinite(v) for v in (target, accept, reject))) or abs(target - (accept - reject)) > 1e-06 | ValueError('Uplift target must equal paired net equity difference') |
| [154](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:154) | Raise | r['label_end'] != r['as_of'] + 21600 | ValueError('Uplift horizon mismatch') |
| [162](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:162) | Raise | len(train) < min_train or len(cal) < 40 or len(test) < 40 | ValueError('Insufficient purged chronological folds') |
| [166](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:166) | Raise | len(np.unique(y > 0)) < 2 or len(np.unique(yc > 0)) < 2 | ValueError('Need both positive and negative uplift episodes') |
| [209](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:209) | Return | No enclosing if; see source try/loop/call context | meta |

### train_uplift.xy

Builds finite feature matrix and target vector; invalid feature_vector raises, no live broker effect.

| Source | Kind | Guard | Expression / caught types |
|---|---|---|---|
| [164](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:164) | Return | No enclosing if; see source try/loop/call context | (np.stack([feature_vector(r['features']) for r in data]), np.array([r['uplift_usd'] for r in data])) |

