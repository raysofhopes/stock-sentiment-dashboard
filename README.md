# 📊 Stock Market Sentiment Dashboard

A Python-based dashboard that analyzes and visualizes sentiment from news headlines or tweets alongside real-time stock performance. Built for showcasing applied data science and financial analysis skills.

## 🚀 Features

- 📈 Fetches historical stock price data using `yfinance`
- 📰 Analyzes sentiment from stock-related news headlines with `TextBlob`
- 📊 Visualizes sentiment trends vs. price trends with `matplotlib` and `seaborn`
- 📂 Clean modular project structure with Jupyter support
- 🖥️ Streamlit-based interactive dashboard (coming soon)

## 🧱 Project Structure

```
├── data/           # Raw or cached datasets
├── notebooks/      # EDA and prototyping notebooks
├── src/            # Python modules (data, sentiment analysis, etc.)
├── dashboard/      # Streamlit dashboard scripts
├── requirements.txt
├── .gitignore
├── README.md
└── venv/           # Virtual environment (excluded from Git)
```

## 🛠️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/stock-sentiment-dashboard.git
cd stock-sentiment-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m textblob.download_corpora
```

## 📌 Technologies Used

- Python 3.11+
- Pandas, NumPy
- yFinance
- TextBlob
- Matplotlib, Seaborn
- Streamlit (for dashboard)

## 📎 License

MIT License