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
    functions_dict = {
        "rsi": rsi,
        "atrr": atr,
    }

    for name in output_names:
        if name in functions_dict:
            entries, exits, fig = functions_dict[name](ta)
            # strategy
            portfolio = vbt.Portfolio.from_signals(
                cac["Close"], entries, exits, init_cash=10000
            )
            fig_portfolio = portfolio.plot()
            tuple_return = (
                col.text(portfolio.stats(silence_warnings=True)),
                container.subheader("Indicator chart"),
                container.plotly_chart(fig, use_container_width=True),
                container.subheader("Strategy chart"),
                container.plotly_chart(fig_portfolio, use_container_width=True),
            )
            return tuple_return
        else:
            tuple_return = ()
            tuple_return = tuple_return + (
                container.text(name),
                container.dataframe(getattr(ta, name)),
            )


def plot_indicator(indicator, entries, exits):
    fig = indicator.vbt.plot()
    entries.vbt.signals.plot_as_entry_markers(indicator, fig=fig)
    exits.vbt.signals.plot_as_exit_markers(indicator, fig=fig)
    return fig


# indicator functions


def rsi(ta):
    entries = ta.rsi_crossed_above(70)
    exits = ta.rsi_crossed_below(30)
    clean_entries, clean_exits = entries.vbt.signals.clean(exits)
    fig = plot_indicator(ta.rsi, clean_entries, clean_exits)
    return entries, exits, fig


def atr(ta):
    # we don't want to trigger buy and sell as atr is just a metric
    entries = ta.atrr_below(20)
    exits = ta.atrr_below(20)
    fig = plot_indicator(ta.atrr, entries, exits)
    return entries, exits, fig
