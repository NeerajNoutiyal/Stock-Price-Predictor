# 📈 Stock Price Predictor

A Machine Learning project that predicts future stock prices using historical stock market data. This project uses **Linear Regression** and **Yahoo Finance (yfinance)** to analyze stock prices and generate predictions through a simple Flask web application.

---

## 🚀 Features

- 📊 Download historical stock data using Yahoo Finance
- 🤖 Train a Linear Regression model
- 📈 Predict future stock prices
- 🌐 User-friendly Flask web interface
- 📉 Visualize stock closing prices

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- yfinance
- Flask
- Joblib

---

## 📂 Project Structure

```
Stock-Price-Predictor/
│── dataset/
│── notebook/
│── screenshots/
│── templates/
│   └── index.html
│── app.py
│── stock_predictor.py
│── train_model.py
│── requirements.txt
│── README.md
│── LICENSE
│── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Stock-Price-Predictor.git
cd Stock-Price-Predictor
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Train the model:

```bash
python train_model.py
```

Run the Flask application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📌 How It Works

1. Downloads historical stock data from Yahoo Finance.
2. Preprocesses the closing price data.
3. Trains a Linear Regression model.
4. Accepts a stock symbol (e.g., AAPL, MSFT, TSLA) from the user.
5. Predicts the next stock price based on the latest available data.

---

## 🔮 Future Improvements

- Support multiple Machine Learning models
- Add LSTM (Deep Learning) prediction
- Display prediction charts
- Deploy the application online
- Improve UI using Bootstrap

---

## 👨‍💻 Author

**Neeraj Noutiyal**
- B.Tech CSE (AI & ML)


---

## 📄 License

This project is licensed under the MIT License.
