import yfinance as yf
import pandas as pd
import pandas_ta as ta

df = pd.DataFrame()

cac_df = df.ta.ticker(
    "^FCHI", start="2020-01-01", end="2022-01-01", timeframe="1d", limit=10000
)

cac_df.drop(labels=["Dividends", "Stock Splits"], axis=1, inplace=True)

print(cac_df.loc[cac_df["Volume"] == 0])
# cac_df.to_csv("data.csv")
