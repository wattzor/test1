```python
# Import necessary libraries
import matplotlib.pyplot as plt

# Load the backtester object from the backtesting file
from backtesting import backtester

# Access the backtest results
results = backtester.results

# Print the profit and loss
print("Profit and Loss: ", results['profit_and_loss'])

# Print the win rate
print("Win Rate: ", results['win_rate'])

# Print the drawdown
print("Drawdown: ", results['drawdown'])

# Plot the equity curve
plt.plot(results['equity_curve'])
plt.title('Equity Curve')
plt.show()
```