import pandas as pd
from strategies.mean_rev import run_mean_reversion
from strategies.direct import run_directional
from strategies.semi_direct import run_semi_directional
from utils.metrics import calculate_metrics
from utils.plotter import plot_equity_curve
from portfolio import combine_portfolios

data = pd.read_csv('data/nifty_options_1y.csv', parse_dates=['datetime'])
data.set_index('datetime', inplace=True)


mr_trades = run_mean_reversion(data)
dir_trades = run_directional(data)
semi_trades = run_semi_directional(data)

print("Mean Reversion:", calculate_metrics(mr_trades))
print("Directional:", calculate_metrics(dir_trades))
print("Semi-Directional:", calculate_metrics(semi_trades))

plot_equity_curve(mr_trades, "Mean Reversion")
plot_equity_curve(dir_trades, "Directional")
plot_equity_curve(semi_trades, "Semi-Directional")

combined = combine_portfolios(mr_trades, dir_trades, semi_trades)
plot_equity_curve(combined, "Combined Strategy")
print("Combined:", calculate_metrics(combined))