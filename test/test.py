import os
from pathlib import Path

import backtrader as bt
import yfinance as yf


class TestStrategy(bt.Strategy):
    def __init__(self):
        self.data_close = self.datas[0].close
        self.order = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            self.log('Buy Executed {}'.format(order.executed.price))
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log("Order Canceled/Margin/Rejected")

        self.order = None

    def next(self):
        self.log('Close: {}'.format(self.data_close[0]))

        if self.order:
            return

        if not self.position:
            if self.data_close[0] > self.data_close[-20]:
                self.log('Buy Order Create {}'.format(self.data_close[0]))
                self.order = self.buy()
        else:
            if self.data_close[0] <= self.data_close[-10]:
                self.log('Sell Order Create{}')
                self.order = self.sell()

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        print('{} {}'.format(dt.isoformat(), txt))


cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

data_path = Path(os.getcwd()) / 'data/US100.csv'
data = bt.feeds.PandasData(dataname=yf.download(
    '^IXIC', '2022-01-01', '2023-01-01'))

cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)

print('S.P: {}'.format(cerebro.broker.getvalue()))

try:
    cerebro.run()
except Exception as e:
    print('例外狀況:', e)

print('F.P: {}'.format(cerebro.broker.getvalue()))

# plotter = btp.PlotlyLinePlotter()
# plotter.plot(result)

cerebro.plot()