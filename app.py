from flask import Flask, render_template, request
import yfinance as yf
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("stock_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    ticker = request.form["ticker"].strip().upper()

    try:
        # Download latest stock data
        stock = yf.download(ticker, period="5d", progress=False)

        if stock.empty:
            return render_template(
                "index.html",
                prediction="❌ Invalid Stock Symbol!"
            )

        # Get latest closing price
        latest_price = float(stock["Close"].iloc[-1])

        # Predict
        input_data = np.array([[latest_price]])
        predicted_price = model.predict(input_data)[0]

        return render_template(
            "index.html",
            prediction=f"📈 Predicted Next Price of {ticker}: ${predicted_price:.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=f"Error: {e}"
        )

if __name__ == "__main__":
    app.run(debug=True)
    app.run(debug=True)
