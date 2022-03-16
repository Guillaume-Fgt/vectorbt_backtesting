from tkinter.tix import COLUMN
from matplotlib import container
import vectorbt as vbt
import pandas as pd
import pandas_ta as ta
import streamlit as st


def calc_ind(col, container, indicator, dict_ind):

    # # # read data
    cac = pd.read_csv("data.csv", index_col=0, parse_dates=True)
    data_set = {"open_", "high", "low", "close", "volume"}

    dict_ind = dict_ind

    # replace value with data[value]
    for i in dict_ind:
        if i in data_set:
            dict_ind[i] = cac[i.title().rstrip("_")]

    # pandas-ta indicator
    TA = vbt.IndicatorFactory.from_pandas_ta(indicator)
    ta = TA.run(**dict_ind)
    output_names = ta.output_names
    tuple_return = ()
    for name in output_names:
        tuple_return = tuple_return + (
            container.text(name),
            container.text(getattr(ta, name)),
        )
    # try:
    #     entries = getattr(ta, indicator).vbt.crossed_above(50)
    #     exits = getattr(ta, indicator).vbt.crossed_below(50)
    # except AttributeError:
    #     return col.text("Not working yet")

    # # see indicator plot with unique entries and exits
    # clean_entries, clean_exits = entries.vbt.signals.clean(exits)
    # fig = plot_indicator(getattr(ta, indicator), clean_entries, clean_exits)

    # # strategy
    # portfolio = vbt.Portfolio.from_signals(
    #     cac["Close"], entries, exits, init_cash=10000
    # )
    # fig_portfolio = portfolio.plot()
    # tuple_return = (
    #     col.text(portfolio.stats(silence_warnings=True)),
    #     container.subheader("Indicator chart"),
    #     container.plotly_chart(fig, use_container_width=True),
    #     container.subheader("Strategy chart"),
    #     container.plotly_chart(fig_portfolio, use_container_width=True),
    # )
    return tuple_return

    # PSL = vbt.IndicatorFactory.from_pandas_ta("psl")
    # psl = PSL.run(cac["Close"], cac["Open"])
    # entries = psl.psl.vbt.crossed_above(50)
    # exits = psl.psl.vbt.crossed_below(50)


def plot_indicator(indicator, entries, exits):
    fig = indicator.vbt.plot()
    entries.vbt.signals.plot_as_entry_markers(indicator, fig=fig)
    exits.vbt.signals.plot_as_exit_markers(indicator, fig=fig)
    return fig


# # strategy plot
# portfolio = vbt.Portfolio.from_signals(cac["Close"], entries, exits, init_cash=10000)
# # portfolio.plot().show()
# print(
#     portfolio.stats(
#         ["total_return", "benchmark_return", "total_trades", "win_rate", "expectancy"]
#     )
# )

# # buy_hold=vbt.Portfolio.from_holding(cac["Close"])
