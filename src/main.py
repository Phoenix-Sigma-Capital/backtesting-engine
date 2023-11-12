import backtrader as bt

# Import your strategy from a separate file (assuming it's named ranging_strategy.py)
from ranging_strategy import RangingStrategy

def run_backtest():
    # Create a Cerebro instance
    cerebro = bt.Cerebro()

    # Add the trading strategy
    cerebro.addstrategy(RangingStrategy)

    # Load the data from CSV file
    data = bt.feeds.GenericCSVData(
        dataname='data/historical/AUDCHF_full_5min.csv',
        fromdate=datetime.datetime(2020, 1, 1),  # Customize dates for your data
        todate=datetime.datetime(2023, 1, 1),
        nullvalue=0.0,
        dtformat=('%Y-%m-%d %H:%M:%S'),
        datetime=0,
        high=2,
        low=3,
        open=1,
        close=4,
        volume=5,
        openinterest=-1
    )

    # Add data to Cerebro
    cerebro.adddata(data)

    # Set initial cash
    cerebro.broker.set_cash(10000)

    # Set the commission - 0.1% ... divide by 100 to remove the %
    cerebro.broker.setcommission(commission=0.001)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run the strategy
    cerebro.run()

    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Plot the result
    cerebro.plot()

if __name__ == '__main__':
    run_backtest()
