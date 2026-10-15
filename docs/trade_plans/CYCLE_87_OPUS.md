[CYCLE_ID: CYCLE_87_START]

Cycle 87 report (matrix as of 11:19:28 UTC): cancel SP500, no new orders

This is the first cycle with real band and wall data for each candidate, so gates 1–4 could be checked directly. The desk-state block still shows stale figures (7,696.86 and 1.53 ATR); I recalculated everything below from the matrix.

Mandate 3: SP500 #18952021 (SELL LIMIT 0.10 @ 7,707.50 / SL 7,718.50 / TP 7,674.50)
Gate	Evidence	Result
Distance	9.12 pts = 1.39 ATR (ATR 6.58), Z +0.86	Pass
1. Stop outside the band	The 7,718.50 stop sits inside the 7,710–7,720 buy-stop cluster (81.8k) and the 7,710–7,720 short-squeeze band (2.3k). Just above sits a 3.375M short-squeeze band at 7,730–7,740, which pulls price up through the stop.	FAIL
3. Unswept stop clusters ahead of entry	The entry is below the unswept 7,710–7,720 buy stops. A sweep of those stops fills the order and then hits the stop: the BTC #18786372 pattern.	FAIL
4. Walls held ≥180s	There are no walls at 7,705–7,715. The only asks are at 7,699.7, 7,700.0 and 7,700.2 (198–248k each). All are MIRRORED_LEG (two-sided), and the longest held is 119.7s.	FAIL
2. CVD	Tick CVD is 1.0 (NEUTRAL), so buyers are not shown to be running out.	Fail
Target	7,674.50 sits inside the 7,670–7,680 band rather than just ahead of the 1.81M sell-stop cluster at 7,680–7,690.	Weak

Can it be fixed? Moving the stop above the magnet means 7,740 + 2.30 = 7,742.30 or higher. That is 34.8 pts of risk, so the order shrinks to 0.04 lot (13.92 USD) for 33 pts of reward, which is 0.95R. That fails.

Ruling: CANCEL. This frees 11.00 USD of risk.

Mandate 2: open positions

There are no open positions.

Mandate 1: candidate screen

Ruled out on the matrix alone:

Model 1 (mean reversion): not allowed anywhere. No asset is in a MEAN_REVERT regime.
SOL: spread 25.43 bps is above the 25 bps limit.
ETH, BNB, BCH: spread ÷ ATR is 0.25, 0.26 and 0.36, above 0.18.
XRP, ADA, DOGE, TRX, DOT, LINK, LTC, AVAX, NEAR: spread above 25 bps and/or 0 whales.
SILVER: spread 6.35 bps is above the 5 bps limit.
DJ30, GER40: 0 whales.
EURUSD, GBPUSD: ATR shows 0.0.

Candidates checked in detail:

Candidate	Proposed levels	Fatal finding
BTC M2 short	Sell the sweep at 81,190, SL 81,343 (above the 81,100–81,200 buy stops of 3.04M, plus 0.35 ATR), TP 80,810. That is 0.09 lot, 13.77 USD, 2.48R.	Gate 2: session CVD has improved from −5.40M to −2.64M and is labelled BULLISH_ABSORPTION, so buyers are absorbing rather than running out. Gate 4: the only walls are top-of-book with 0s held.
ETH M2 short	0.60 lot @ 2,377.0 / SL 2,398.5 (above the 14.69M ask at 2,392.9 plus 0.35 ATR) / TP 2,348.0 (just ahead of the 7.42M bid at 2,346.5).	1.38R, below 2.0. The nearer target at 2,361 (the 4.08M sell stops) gives only 0.76R. The L3 walls show maker=N/A and no hold time.
USDJPY M2 short (card from the last cycle)	0.13 @ 157.880 / SL 158.050 / TP 157.540	Gate 1: the stop is inside the 158.0–159.0 buy-stop bucket. That bucket is 1.0 JPY wide (about 10 ATR), which is too coarse to place a stop against, and putting the stop above 159.035 gives about 0.3R. Gate 2: tick CVD shows BUYER_AGGRESSION. Gate 4: the 157.88 ask has held 609s, but its notional is exactly 157,880, which equals price × 1,000 and looks like a placeholder. It is also 0.16M, well below 3M.
NAS100 M2 short	Entry 29,616 (below the asks at 29,617–29,619)	The stop must clear the 29,600–29,700 band plus 0.35 ATR, so 29,718 or higher. That is 102 pts × 0.20 = 20.40 USD at minimum lot, above 14.50. The asks are MIRRORED_LEG.
GOLD M2 long	Pullback to VWAP	Every wall has held 0.0s. Price is stretched at +1.56σ. The sell-stop bands below are negligible (under 2k).
USWTI M2 long	–	Price is stretched at +1.93σ. Walls have held 0s and are mirrored. The band levels sit near 94, against a mid of 95.136: they come from a different venue about 1.16 lower, so the mapping needs checking.
Bracket
Round	Winner	Loser	Deciding factor
QF1	ETH short	USDJPY short	USDJPY fails gates 1, 2 and 4; ETH is the only candidate with walls of 3M or more
QF2	BTC short	NAS100 short	NAS100 fails on sizing
QF3	GOLD long	USWTI long	friction 0.012 against 0.153
SF	ETH	BTC	BTC fails the CVD gate (absorption is the wrong way for a short)
SF	ETH	GOLD	GOLD fails on wall hold time and on location
Final	ETH short	–	It still fails: 1.38R is below 2.0R, and wall hold time can't be verified

Result: no candidate passes all 5 gates.

Watchlist only, do not stage
SP500 sweep-and-fade short. SELL LIMIT 0.14 @ 7,739.5 / SL 7,749.4 / TP 7,693.9.
Risk 13.86 USD, reward about 63.84 USD, 4.6R.
The stop is 1.5 ATR away and clears the 7,740 band by 1.4 ATR. The target front-runs the 1.81M sell stops at 7,680–7,690.
Price is 6.2 ATR from entry today. Stage it only when price is within 2.0 ATR and a one-sided ask wall of 3M or more has held 180s or longer near 7,740 and buyers are running out.
ETH short. Usable only if the target can run through the 7.42M bid at 2,346.5 to the 3.0M band at 2,330–2,340 and still reach 2.0R or better, and the walls show a maker and a hold time.
Capital (Persona C)
Book	Risk incl. 2.00 USD reserve per ticket	Worst-case equity	Above floor / buffer
As staged	13.00	4,846.55	+71.55 / +51.55
After cancelling	0	4,859.55	+84.55 / +64.55
Flat book plus 3 tickets at 14.50	49.50	4,810.05	+35.05 / +15.05
Rulings
#18952021: CANCEL. The stop is inside a band, a 3.375M magnet sits just above it, and the walls don't exist.
New orders: none. SP500 sweep-and-fade and ETH stay on the watchlist.
Open positions: none. The book should be flat at 4,859.55 USD with 4 of 4 slots free.
Desk fixes:
Tag L3 walls with the maker and hold time.
Fix the 1.0-JPY-wide FX bucketing.
Remove the price × 1,000 placeholder notional.
Fix the 0.0 ATR on EURUSD and GBPUSD.

[CYCLE_ID: CYCLE_87_COMPLETE]