import pandas_datareader.data as web
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# --- Parameters ---
TICKER = "AAPL"
START_DATE = "2023-01-01"
END_DATE = datetime.today().strftime("%Y-%m-%d")
TODAY = datetime.today().date()
API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"  # Replace with your actual API key

NEWS_HEADLINES = [
    "Apple stock jumps as new iPhone is revealed.",
    "Apple faces legal battle over patent dispute.",
    "Strong demand for Apple services drives revenue.",
    "Investors worry about supply chain disruption at Apple.",
    "Apple exceeds Wall Street expectations."
]

# --- Simulate Sentiment Over Past Weeks ---
df_sentiment = pd.DataFrame({
    'Date': [TODAY - timedelta(days=7 * i) for i in range(len(NEWS_HEADLINES))],
    'Headline': NEWS_HEADLINES,
    'Sentiment': [TextBlob(h).sentiment.polarity for h in NEWS_HEADLINES]
})
df_sentiment_avg = df_sentiment.groupby('Date', as_index=False)['Sentiment'].mean()

# --- Fetch stock price using Alpha Vantage ---
df_price = web.DataReader(TICKER, 'av-daily', start=START_DATE, api_key=API_KEY)
df_price = df_price.reset_index()
df_price.rename(columns={'index': 'Date', 'close': 'Close'}, inplace=True)
df_price['Date'] = pd.to_datetime(df_price['Date']).dt.date
df_price = df_price[['Date', 'Close']]

# --- Merge data ---
df_combined = pd.merge(df_price, df_sentiment_avg, on='Date', how='left')

# --- Plot ---
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(df_combined["Date"], df_combined["Close"], color="blue", label="Stock Price")
ax1.set_ylabel("Stock Price", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

ax2 = ax1.twinx()
sentiment_data = df_combined.dropna(subset=["Sentiment"])
ax2.scatter(sentiment_data["Date"], sentiment_data["Sentiment"], color="orange", s=100, label="Sentiment")
ax2.set_ylabel("Sentiment Score", color="orange")
ax2.tick_params(axis="y", labelcolor="orange")

plt.title("AAPL Stock Price vs News Sentiment (Simulated)")
fig.tight_layout()
plt.show()