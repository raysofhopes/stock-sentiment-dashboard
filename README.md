
# 📈 Stock Sentiment Dashboard

A simple yet insightful dashboard that visualizes the correlation between stock price movement and news sentiment. This project uses historical stock price data and basic sentiment analysis on sample headlines to simulate market sentiment and display trends interactively.

## 🔍 Overview

This project:

- Pulls historical stock data for a given ticker using `pandas_datareader` (Alpha Vantage API).
- Performs sentiment analysis on curated headlines using `TextBlob`.
- Aligns sentiment scores with historical stock prices for visual comparison.
- Generates an Excel report with combined data.
- Visualizes stock price and sentiment scores using Matplotlib and Seaborn.

## 🧪 Technologies Used

- Python 3.11
- pandas
- matplotlib
- seaborn
- textblob
- pandas_datareader
- openpyxl

## 📊 Sample Output

![Dashboard Preview](screenshots/sample_plot.png)  
> *Note: Sentiment values are simulated and not tied to real news APIs.*

## 📁 Project Structure

```
stock-sentiment-dashboard/
├── data/                  # Raw or future real data
├── notebooks/             # Optional Jupyter experiments
├── output/                # Exported Excel files
├── src/                   # Core logic
│   └── sentiment_engine.py
├── venv/                  # Virtual environment (not uploaded to GitHub)
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

## 📦 Installation

```bash
git clone https://github.com/your-username/stock-sentiment-dashboard.git
cd stock-sentiment-dashboard
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 🚀 Run the App

```bash
python src/sentiment_engine.py
```

Make sure you replace `API_KEY` in the script with your [Alpha Vantage](https://www.alphavantage.co/support/#api-key) key.

## 📤 Output

An Excel file is saved in `/output/stock_sentiment_output.xlsx` and a plot visualizes the data comparison.

## ✅ Future Enhancements

- Connect to real-time news sentiment APIs.
- Add Streamlit or Dash interface for interaction.
- Extend for multiple tickers and sectors.
