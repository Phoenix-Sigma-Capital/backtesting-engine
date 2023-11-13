import backtrader as bt

# Define your strategy
class RangingStrategy(bt.Strategy):
    params = (('rsi_period', 14), ('bollinger_period', 20), ('obv_period', 20))

    def __init__(self):
        # Initialize indicators
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=self.params.rsi_period)
        self.bollinger = bt.indicators.BollingerBands(self.data.close, period=self.params.bollinger_period)
        self.obv = bt.indicators.OnBalanceVolume(self.data, period=self.params.obv_period)

    def next(self):
        # Define your strategy logic
        if not self.position:
            if self.rsi < 30 and self.data.close < self.bollinger.lines.bot:
                self.buy()
        elif self.rsi > 70 and self.data.close > self.bollinger.lines.top:
            self.sell()

if __name__ == '__main__':
    # Initialize and configure backtrader Cerebro engine
    cerebro = bt.Cerebro()
    cerebro.addstrategy(RangingStrategy)

    # Load data
    data = bt.feeds.GenericCSVData(
        dataname='data/historical/AUDCHF_full_5min.csv',
        datetime=0,
        open=1,
        high=2,
        low=3,
        close=4,
        volume=5,
        timeframe=bt.TimeFrame.Minutes,
        compression=5
    )

    # Add data to Cerebro
    cerebro.adddata(data)

    # Run the strategy
    cerebro.run()

    # Plot the results
    cerebro.plot()
