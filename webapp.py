import streamlit as st
import pandas_ta as ta
import pandas as pd
import inspect
from pandas_ta_utils import list_ind
from strategy import calc_ind


def main():
    st.header("Cac40 backtesting")

    col1, col2 = st.columns([2, 5])
    # container: will be used by callback function calc_ind to populate the page
    cont = st.container()
    cont.write("")
    with col1:
        # List of all indicators
        indicators = list_ind()
        select_ind = st.selectbox("Choose a pandas-ta indicator", indicators)

        ind_function = getattr(ta, select_ind)
        st.sidebar.write(ind_function.__doc__)

        arguments = inspect.getfullargspec(ind_function)
        list_arg = {}
        for argument in arguments.args:
            name_textin = f"{argument}input"
            # toggle type of input according to variable. Data will be automatically added, no need to enter infos
            data_set = {"open_", "high", "low", "close", "volume"}
            text_set = {"mamode"}
            bool_set = {"talib"}
            if argument in text_set:
                name_textin = st.text_input(argument)
            elif argument in bool_set:
                name_textin = st.radio(argument, options=(True, False))
            elif argument not in data_set:
                name_textin = st.number_input(argument, step=1)
            list_arg[argument] = name_textin
        st.button("Submit", on_click=calc_ind, args=(col2, cont, select_ind, list_arg))
