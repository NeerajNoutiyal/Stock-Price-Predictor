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
        stock = yf.download(
            ticker,
            period="5d",
            auto_adjust=True,
            progress=False
        )

        if stock.empty:
            return render_template(
                "index.html",
                prediction="❌ Invalid Stock Symbol!"
            )

        # Get latest closing price safely
        close = stock["Close"]

        # Handle DataFrame or Series
        if hasattr(close, "columns"):
            latest_price = close.iloc[-1, 0]
        else:
            latest_price = close.iloc[-1]

        latest_price = float(latest_price)

        # Predict
        prediction = model.predict(np.array([[latest_price]]))[0]

        return render_template(
            "index.html",
            prediction=f"📈 Predicted Next Price for {ticker}: ${prediction:.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)
    
