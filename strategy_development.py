```python
import pandas as pd
from data_preparation import data

# Calculate the moving averages
data['MA10'] = data['Close'].rolling(window=10).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

class Strategy:
    def __init__(self, data):
        self.data = data

    def buy_signal(self):
        # Buy when the 10-day moving average crosses above the 50-day moving average
        buy_signal = (self.data['MA10'] > self.data['MA50']) & (self.data['MA10'].shift(1) < self.data['MA50'].shift(1))
        return buy_signal

    def sell_signal(self):
        # Sell when the 10-day moving average crosses below the 50-day moving average
        sell_signal = (self.data['MA10'] < self.data['MA50']) & (self.data['MA10'].shift(1) > self.data['MA50'].shift(1))
        return sell_signal

# Instantiate the strategy object
strategy = Strategy(data)
```