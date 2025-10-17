# Technical Documentation: Nifty Options Intraday Backtesting

## Overview

This project implements three intraday trading strategies on 1-minute Nifty options data:

- **Mean Reversion**: Buys when price dips below a rolling average.
- **Directional Momentum**: Buys when price shows upward momentum.
- **Semi-Directional Volatility**: Buys during high volatility bursts.

Each strategy is evaluated using performance metrics and visualized via equity curves.

---

## Components

### 1. `main.py`
- Loads and cleans the dataset
- Runs all three strategies
- Computes metrics and plots equity curves
- Combines portfolios for final evaluation

### 2. `strategies/`
- `mean_rev.py`: Implements mean reversion logic
- `direct.py`: Implements directional momentum logic
- `semi_direct.py`: Implements volatility-based logic

### 3. `utils/`
- `metrics.py`: Calculates CAGR, Sharpe, Calmar, Drawdown, Win Rate, Avg P/L
- `plotter.py`: Saves equity curve plots to `visualizations/`

### 4. `portfolio.py`
- Combines multiple strategy outputs into a unified portfolio

---

## Metrics Calculated

- **CAGR**: Compound Annual Growth Rate
- **Max Drawdown**: Largest peak-to-trough decline
- **Sharpe Ratio**: Risk-adjusted return
- **Win Rate**: Percentage of profitable trades
- **Avg P/L**: Average profit/loss per trade
- **Calmar Ratio**: CAGR / Max Drawdown

---

## Visualizations

Equity curves are saved in the `visualizations/` folder:

- `mean_reversion_equity_curve.png`
- `directional_equity_curve.png`
- `semi_directional_equity_curve.png`
- `combined_strategy_equity_curve.png`
- `Output.png`

---

## Data Format

Expected CSV columns (all lowercase):
`datetime`, `open`, `high`, `low`, `close`, `volume`
Ensure `datetime` is parsed as a timestamp and set as index.

---

