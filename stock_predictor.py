import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Download stock data
stock = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

# Keep required columns
data = stock[['Close']].copy()

# Create prediction column
data['Prediction'] = data[['Close']].shift(-30)

# Remove last 30 rows
X = data[['Close']][:-30]
y = data['Prediction'][:-30]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict next price
prediction = model.predict([[stock['Close'].iloc[-1]]])

print("Predicted Next Price:", prediction[0])

# Plot closing price
plt.figure(figsize=(10,5))
plt.plot(stock['Close'])
plt.title("Apple Stock Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
