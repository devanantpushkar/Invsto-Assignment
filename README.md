# Stock Price Prediction Pipeline

A comprehensive data science pipeline for analyzing, visualizing, and predicting stock market prices. This project automates the workflow from data acquisition to model evaluation, providing actionable insights through a detailed report.

## Features

- **Automated Data Processing**: Fetches daily OHLC data for 20+ diverse equities and cleanses it for analysis.
- **Exploratory Data Analysis (EDA)**: Generates historical price visualizations to identify trends and patterns.
- **Advanced Modeling**:
  - **ARIMA**: Statistical time-series forecasting with automated order selection.
  - **Gradient Boosting**: Machine learning regression using technical indicators (SMA, RSI, Volatility).
- **Performance Evaluation**: Compares models using RMSE, MAE, and MAPE metrics.
- **Report Generation**: Automatically compiles all findings, charts, and metrics into a formatted Markdown report.

## Project Structure

```text
/
├── data_processor.py      # Data loading, cleaning, and feature engineering
├── generate_dataset.py    # Script to download stock data via yfinance
├── models.py             # ARIMA and Gradient Boosting model implementations
├── report_generator.py    # Utility for creating the Markdown report
├── run_pipeline.py        # Main entry point for the analysis pipeline
├── visualization.py       # Plotting utilities for EDA and predictions
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Installation

Ensure you have Python 3.8 or higher installed.

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Generate Dataset

First, download the latest stock data for the defined tickers. This will save CSV files to the `stock_data/` directory.

```bash
python generate_dataset.py
```

### 2. Run the Analysis Pipeline

Execute the main pipeline to process data, train models, and generate the report.

```bash
python run_pipeline.py
```

**Options:**

- `--tickers`: Specify one or more tickers to analyze (default: processes a subset of 3 tickers for demonstration).
- `--data_dir`: Directory containing input CSV files (default: `stock_data`).
- `--output_dir`: Directory to save results and figures (default: `results`).

**Examples:**

Run the pipeline (defaults to first 3 tickers):
```bash
python run_pipeline.py
```

Run for specific stocks:
```bash
python run_pipeline.py --tickers AAPL MSFT TSLA
```

## Results

After execution, the results will be available in the `results/` directory:

- **`results/report.md`**: The complete analysis report.
- **`results/figures/`**: Generated plots for historical prices, predictions, and feature importance.
