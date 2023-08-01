```python
import pandas as pd

# Load the data from data_retrieval.py
data = pd.read_csv('data.csv')

# Remove any rows with missing values
data = data.dropna()

# Remove any outliers based on standard deviation
data = data[(np.abs(stats.zscore(data)) < 3).all(axis=1)]

# Select the 'Close' column for analysis
data = data['Close']

# Save the cleaned and preprocessed data
data.to_csv('cleaned_data.csv', index=False)
```