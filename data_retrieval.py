```python
import yfinance as yf

# Define the symbol, start date, and end date
symbol = "AAPL"
start_date = "2021-01-01"
end_date = "2021-12-31"

# Download the data
data = yf.download(symbol, start=start_date, end=end_date)

# Save the data to a csv file for further use
data.to_csv('trading_data.csv')
```