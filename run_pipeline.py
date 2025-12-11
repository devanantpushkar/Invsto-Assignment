import os
import argparse
from data_processor import DataProcessor
from visualization import Visualizer
from models import ArimaPredictor, GradientBoostingPredictor
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="Stock Price Prediction Pipeline")
    parser.add_argument("--data_dir", type=str, default="stock_data", help="Directory containing stock CSVs")
    parser.add_argument("--output_dir", type=str, default="results", help="Directory for output results")
    parser.add_argument("--tickers", type=str, nargs='+', help="Specific tickers to process (default: all)")
    args = parser.parse_args()

    data_dir = args.data_dir
    output_dir = args.output_dir
    figures_dir = os.path.join(output_dir, "figures")
    
    os.makedirs(figures_dir, exist_ok=True)
    
    processor = DataProcessor(data_dir)
    visualizer = Visualizer(figures_dir)
    report = ReportGenerator(os.path.join(output_dir, "report.md"))
    
    report.add_header("Stock Price Prediction Analysis Report", level=1)
    
    tickers = args.tickers if args.tickers else processor.get_all_tickers()
    
    # Process a subset if no specific tickers provided to save time for demonstration,
    # or process all if the user wants. The prompt asks for "at least one", so let's do up to 3.
    if not args.tickers:
        tickers = tickers[:3] 
        print(f"Processing first 3 tickers: {tickers}")

    for ticker in tickers:
        print(f"Processing {ticker}...")
        report.add_header(f"Analysis for {ticker}", level=2)
        
        try:
            # 1. Data Loading & Cleaning
            df = processor.load_data(ticker)
            df = processor.clean_data(df)
            
            # 2. Visualization (EDA)
            hist_plot = visualizer.plot_stock_history(df, ticker)
            report.add_text(f"### Historical Price for {ticker}")
            report.add_image(hist_plot, f"{ticker} History")
            
            # 3. Feature Engineering
            df_features = processor.feature_engineering(df)
            
            # 4. Modeling
            X_train, y_train, X_test, y_test = processor.train_test_split_time(df_features)
            
            # ARIMA
            print(f"  Training ARIMA for {ticker}...")
            arima = ArimaPredictor()
            arima.fit(y_train)
            y_pred_arima = arima.predict(len(y_test))
            # Align ARIMA preds with test index
            y_pred_arima.index = y_test.index
            
            arima_metrics = arima.evaluate(y_test, y_pred_arima)
            report.add_metrics_table(arima_metrics, title=f"ARIMA Performance - {ticker}")
            
            arima_plot = visualizer.plot_predictions(y_test, y_pred_arima, ticker, "ARIMA")
            report.add_image(arima_plot, f"{ticker} ARIMA Predictions")
            
            # Gradient Boosting
            print(f"  Training Gradient Boosting for {ticker}...")
            gb = GradientBoostingPredictor()
            gb.fit(X_train, y_train)
            y_pred_gb = gb.predict(X_test)
            
            gb_metrics = gb.evaluate(y_test, y_pred_gb)
            report.add_metrics_table(gb_metrics, title=f"Gradient Boosting Performance - {ticker}")
            
            gb_plot = visualizer.plot_predictions(y_test, y_pred_gb, ticker, "GradientBoosting")
            report.add_image(gb_plot, f"{ticker} Gradient Boosting Predictions")
            
            feat_imp_plot = visualizer.plot_feature_importance(gb.model, X_train.columns, ticker)
            if feat_imp_plot:
                report.add_image(feat_imp_plot, f"{ticker} Feature Importance")

            # Comparison Text
            report.add_text(f"**Comparison**: ")
            rmse_diff = arima_metrics['RMSE'] - gb_metrics['RMSE']
            if rmse_diff > 0:
                report.add_text(f"Gradient Boosting performed better by RMSE diff of {rmse_diff:.4f}.")
            else:
                report.add_text(f"ARIMA performed better by RMSE diff of {-rmse_diff:.4f}.")
                
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
            report.add_text(f"Error processing {ticker}: {e}")
            
    report.save()
    print(f"Analysis complete. Report saved to {os.path.join(output_dir, 'report.md')}")

if __name__ == "__main__":
    main()
