import yfinance as yf
import joblib
from sklearn.linear_model import LinearRegression

# Download stock data
stock = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

data = stock[['Close']].copy()
data['Prediction'] = data[['Close']].shift(-30)

X = data[['Close']][:-30]
y = data['Prediction'][:-30]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "stock_model.pkl")

print("Model Saved Successfully!")
