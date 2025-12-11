import pandas as pd
import numpy as np
import os
import glob

class DataProcessor:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_data(self, ticker):
        file_path = os.path.join(self.data_dir, f"{ticker}.csv")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found for ticker: {ticker}")
        
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.set_index('Date').sort_index()
        return df

    def get_all_tickers(self):
        files = glob.glob(os.path.join(self.data_dir, "*.csv"))
        return [os.path.splitext(os.path.basename(f))[0] for f in files]

    def clean_data(self, df):
        df = df.replace([np.inf, -np.inf], np.nan)
        df = df.interpolate(method='time')
        df = df.fillna(method='bfill').fillna(method='ffill')
        return df

    def feature_engineering(self, df):
        df = df.copy()
        
        df['Return'] = df['Close'].pct_change()
        
        for lag in [1, 2, 3, 5]:
            df[f'Lag_{lag}'] = df['Close'].shift(lag)
        
        for window in [7, 14, 30]:
            df[f'Rolling_Mean_{window}'] = df['Close'].rolling(window=window).mean()
            df[f'Rolling_Std_{window}'] = df['Close'].rolling(window=window).std()
            
        df = df.dropna()
        return df

    def train_test_split_time(self, df, target_col='Close', test_size=0.2):
        split_idx = int(len(df) * (1 - test_size))
        train = df.iloc[:split_idx]
        test = df.iloc[split_idx:]
        
        X_train = train.drop(columns=[target_col])
        y_train = train[target_col]
        X_test = test.drop(columns=[target_col])
        y_test = test[target_col]
        
        return X_train, y_train, X_test, y_test
