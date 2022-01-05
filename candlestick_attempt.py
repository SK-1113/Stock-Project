import yfinance
import plotly.graph_objects as go
from plotly.subplots import make_subplots

tsla = yfinance.Ticker('TSLA')
hist = tsla.history(period = '1y')
#print(hist.head())

#Basic scatter plot
#fig = go.Figure(data=go.Scatter(x=hist.index,y=hist['Close']))

#Basic scatter plot w/ mode = 'markers'
fig = go.Figure(data = go.Scatter(x = hist.index, y = hist['Close'], mode = 'lines + markers'))

#fig.show()

#ADDING TRADE VOLUME TO STOCK CHARTS
fig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2.add_trace(go.Scatter(x=hist.index,y=hist['Close'],name='Price'),secondary_y=False)
fig2.add_trace(go.Bar(x=hist.index,y=hist['Volume'],name='Volume'),secondary_y=True)

#scaling the y-axis to make the volume bars smaller
fig2.update_yaxes(range=[0,700000000],secondary_y=True)
fig2.update_yaxes(visible=False, secondary_y=True)
#fig2.show()

#CANDLESTICK CHART

fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Candlestick(x=hist.index, open=hist['Open'],
                              high=hist['High'],
                              low=hist['Low'],
                              close=hist['Close'],
                             ))

fig3.add_trace(go.Bar(x=hist.index, y=hist['Volume'], name='Volume'),secondary_y=True)
fig3.update_layout(xaxis_rangeslider_visible=False)
