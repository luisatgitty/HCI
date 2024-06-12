# Import necessary libraries
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Define a simple time series for testing purposes
series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Define the ARIMA model
model = ARIMA(series, order=(5,1,0))

# Fit the model
model_fit = model.fit()

# Make predictions
predictions = model_fit.predict(len(series), len(series)+5)

# Print out the predictions
print(predictions)

input("Press Enter to exit...")