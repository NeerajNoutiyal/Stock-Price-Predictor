import joblib
import yfinance as yf
from flask import Flask, render_template, request

app = Flask(__name__)

# Load trained model
model = joblib.load("stock_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    ticker = request.form["ticker"].upper()

    stock = yf.download(ticker, period="5d")

    if stock.empty:
        return render_template("index.html", prediction="Invalid Stock Symbol!")

    latest_price = stock["Close"].iloc[-1]

    predicted_price = model.predict([[latest_price]])

    return render_template(
        "index.html",
        prediction=f"Predicted Next Price for {ticker}: ${predicted_price[0]:.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)
