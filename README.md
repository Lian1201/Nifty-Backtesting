# Nifty Options Intraday Backtesting

This repository contains a complete backtesting framework for evaluating intraday trading strategies on Nifty options using 1-minute data.

## Project Overview

We implement and compare three strategies:

- **Mean Reversion**
- **Directional Momentum**
- **Semi-Directional Volatility**

Each strategy is evaluated using:

- Cumulative P&L
- CAGR, Sharpe Ratio, Calmar Ratio
- Max Drawdown, Win Rate, Avg P/L

## Project Structure
```
nifty_options_backtest/ 
├── data/ 
│   └── nifty_options_1y.csv 
├── visualizations/ 
│   ├── mean_reversion_equity_curve.png 
│   ├── directional_equity_curve.png 
│   ├── semi_directional_equity_curve.png 
│   └── combined_strategy_equity_curve.png 
├── strategies/ 
│   ├── mean_rev.py 
│   ├── direct.py 
│   └── semi_direct.py 
├── utils/ 
│   ├── metrics.py 
│   └── plotter.py 
├── portfolio.py 
├── main.py 
├── requirements.txt 
├── README.md 
├── TECHNICAL_DOCUMENTATION.md
```

## 🛠️ Setup Instructions

### 1. Clone the repo:
   ```bash
   git clone https://github.com/Lian1201/Nifty-Backtesting.git
   cd Nifty-Backtesting
   ```

### 2. 	Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

### 3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
### 4. Run the backtest:
   ```bash
   python main.py
   ```



