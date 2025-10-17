import pandas as pd

def combine_portfolios(*dfs):
    combined = pd.concat(dfs).sort_values(by='entry_time')
    combined.reset_index(drop=True, inplace=True)
    return combined