# Stock Price Prediction Analysis Report

## Analysis for AAPL

### Historical Price for AAPL

![AAPL History](figures\AAPL_history.png)

### ARIMA Performance - AAPL

| Metric | Value |
|---|---|
| RMSE | 45.7332 |
| MAE | 41.0967 |
| MAPE | 0.1581 |
| Order | (0, 1, 2) |


![AAPL ARIMA Predictions](figures\AAPL_ARIMA_prediction.png)

### Gradient Boosting Performance - AAPL

| Metric | Value |
|---|---|
| RMSE | 11.4760 |
| MAE | 7.4672 |
| MAPE | 0.0276 |


![AAPL Gradient Boosting Predictions](figures\AAPL_GradientBoosting_prediction.png)

![AAPL Feature Importance](figures\AAPL_feature_importance.png)

**Comparison**: 

Gradient Boosting performed better by RMSE diff of 34.2572.

## Analysis for AMD

### Historical Price for AMD

![AMD History](figures\AMD_history.png)

### ARIMA Performance - AMD

| Metric | Value |
|---|---|
| RMSE | 41.6632 |
| MAE | 33.5467 |
| MAPE | 0.1542 |
| Order | (0, 1, 0) |


![AMD ARIMA Predictions](figures\AMD_ARIMA_prediction.png)

### Gradient Boosting Performance - AMD

| Metric | Value |
|---|---|
| RMSE | 20.8185 |
| MAE | 12.9213 |
| MAPE | 0.0546 |


![AMD Gradient Boosting Predictions](figures\AMD_GradientBoosting_prediction.png)

![AMD Feature Importance](figures\AMD_feature_importance.png)

**Comparison**: 

Gradient Boosting performed better by RMSE diff of 20.8447.

## Analysis for AMZN

### Historical Price for AMZN

![AMZN History](figures\AMZN_history.png)

### ARIMA Performance - AMZN

| Metric | Value |
|---|---|
| RMSE | 9.2956 |
| MAE | 7.3145 |
| MAPE | 0.0323 |
| Order | (0, 1, 0) |


![AMZN ARIMA Predictions](figures\AMZN_ARIMA_prediction.png)

### Gradient Boosting Performance - AMZN

| Metric | Value |
|---|---|
| RMSE | 2.7811 |
| MAE | 1.6799 |
| MAPE | 0.0072 |


![AMZN Gradient Boosting Predictions](figures\AMZN_GradientBoosting_prediction.png)

![AMZN Feature Importance](figures\AMZN_feature_importance.png)

**Comparison**: 

Gradient Boosting performed better by RMSE diff of 6.5144.
