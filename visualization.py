import matplotlib.pyplot as plt
import seaborn as sns
import os

class Visualizer:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
    def plot_stock_history(self, df, ticker):
        plt.figure(figsize=(14, 7))
        plt.plot(df.index, df['Close'], label='Close Price')
        plt.title(f'{ticker} Stock Price History')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        
        save_path = os.path.join(self.output_dir, f"{ticker}_history.png")
        plt.savefig(save_path)
        plt.close()
        return save_path

    def plot_predictions(self, y_true, y_pred, ticker, model_name):
        plt.figure(figsize=(14, 7))
        plt.plot(y_true.index, y_true, label='Actual')
        plt.plot(y_true.index, y_pred, label='Predicted', linestyle='--')
        plt.title(f'{ticker} Price Prediction - {model_name}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        
        save_path = os.path.join(self.output_dir, f"{ticker}_{model_name}_prediction.png")
        plt.savefig(save_path)
        plt.close()
        return save_path

    def plot_feature_importance(self, model, feature_names, ticker):
        if not hasattr(model, 'feature_importances_'):
            return None
            
        importance = model.feature_importances_
        indices = importance.argsort()[::-1]
        
        plt.figure(figsize=(10, 6))
        plt.title(f'Feature Importance - {ticker}')
        plt.bar(range(len(indices)), importance[indices], align='center')
        plt.xticks(range(len(indices)), [feature_names[i] for i in indices], rotation=45)
        plt.tight_layout()
        
        save_path = os.path.join(self.output_dir, f"{ticker}_feature_importance.png")
        plt.savefig(save_path)
        plt.close()
        return save_path
