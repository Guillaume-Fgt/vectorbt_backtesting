import pandas_ta as ta
import pandas as pd
import vectorbt as vbt

# List of all indicators
def list_ind():
    df = pd.DataFrame()
    indicators = ta.AnalysisIndicators(df).indicators(as_list=True)
    return indicators


# cac = pd.read_csv("data.csv", index_col=0, parse_dates=True)

# # abb = ta.aberration(cac["High"], cac["Low"], cac["Close"])
# # print(abb)
# df = pd.DataFrame()
# TA = vbt.IndicatorFactory.from_pandas_ta("aberration")
# abb = TA.run(cac["High"], cac["Low"], cac["Close"])
# print(abb.output_names)
# abb = ta.atr(cac["High"], cac["Low"], cac["Close"])
# print(abb)

# TA = vbt.IndicatorFactory.from_pandas_ta("atr")
# atr = TA.run(cac["High"], cac["Low"], cac["Close"], short_name="atr")
# print(dir(atr))

# TA = vbt.IndicatorFactory.from_pandas_ta("psl")
# psl = TA.run(cac["Close"], cac["Open"])
# print(dir(psl))

# TA = vbt.IndicatorFactory.from_pandas_ta("rsi")
# rsi = TA.run(cac["Close"])
# print(dir(rsi))
