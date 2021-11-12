import plotly.graph_objects as go

import pandas as pd
from datetime import datetime

df=pd.read_csv('apple_stock_data.csv')

fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

fig.update_xaxes(
    rangebreaks=[
            # NOTE: Below values are bound (not single values), ie. hide x to y
            dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
            # dict(bounds=[17, 9], pattern="hour"),  # h

            # dict(values=["2019-12-25", "2020-12-24"])  # hide holidays (Christmas and New Year's, etc)
        ]
)



fig.update_layout(
    title='Zifeng An',
    yaxis_title='AAPL Stock'

)

fig.show()