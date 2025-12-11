import yfinance as yf
import os
import pandas as pd

# List of 20 diverse equities
tickers = [
    # Tech
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA",
    # Finance
    "JPM", "BAC", "V", "MA",
    # Healthcare
    "JNJ", "PFE", "UNH",
    # Energy
    "XOM", "CVX",
    # Consumer
    "KO", "PEP",
    # Entertainment
    "DIS", "NFLX",
    # Semiconductors
    "NVDA", "AMD"
]

output_dir = "stock_data"
os.makedirs(output_dir, exist_ok=True)

print(f"Downloading data for {len(tickers)} tickers...")

for ticker in tickers:
    print(f"Downloading {ticker}...")
    try:
        # Download last 2 years of daily data
        df = yf.download(ticker, period="2y", interval="1d", progress=False)
        
        if not df.empty:
            # Flatten multi-level columns if they exist (yfinance update)
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            
            # Save to CSV
            file_path = os.path.join(output_dir, f"{ticker}.csv")
            df.to_csv(file_path)
            print(f"Saved {ticker} to {file_path}")
        else:
            print(f"No data found for {ticker}")
            
    except Exception as e:
        print(f"Error downloading {ticker}: {e}")

print("Download complete.")
