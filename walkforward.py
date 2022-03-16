import vectorbt as vbt
import numpy
import pandas

# get data
cac_price = vbt.YFData.download(
    "^FCHI", start="2017-01-01", end="2022-01-01", timeframe="1d", limit=10000
)
price = cac_price.get("Close")
# figure = price.vbt.plot(trace_names=["Price"], width=1280, height=720)
# figure.show()

# windows = numpy.arange(10, 50)
# fast_ma, slow_ma = vbt.MA.run_combs(price, windows)
# entries = fast_ma.ma_crossed_above(slow_ma)
# exits = fast_ma.ma_crossed_below(slow_ma)

# portfolio = vbt.Portfolio.from_signals(
#     price, entries, exits, freq="1d", direction="both"
# )

# print(portfolio.total_return().sort_values())

# figure = price.vbt.rolling_split(
#     n=20, window_len=360, set_lens=(108,), left_to_right=False, plot=True
# )
# figure.update_layout(width=1280, height=720)
# figure.show()
(in_sample_prices, in_sample_dates), (
    out_sample_prices,
    out_sample_dates,
) = price.vbt.rolling_split(n=20, window_len=360, set_lens=(108,), left_to_right=False)

windows = numpy.arange(10, 50)
fast_ma, slow_ma = vbt.MA.run_combs(in_sample_prices, windows)
entries = fast_ma.ma_crossed_above(slow_ma)
exits = fast_ma.ma_crossed_below(slow_ma)

portfolio = vbt.Portfolio.from_signals(
    in_sample_prices, entries, exits, freq="1d", direction="both"
)

performance = portfolio.sharpe_ratio()

print(performance[performance.groupby("split_idx").idxmax()].index)
