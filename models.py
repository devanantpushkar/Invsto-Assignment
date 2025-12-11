from statsmodels.tsa.arima.model import ARIMA
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from sklearn.model_selection import GridSearchCV
import numpy as np
import warnings

warnings.filterwarnings("ignore")

class ArimaPredictor:
    def __init__(self):
        self.model = None
        self.order = None

    def find_best_order(self, data):
        best_aic = float('inf')
        best_order = (1, 1, 1)
        p_values = range(0, 3)
        d_values = range(0, 2)
        q_values = range(0, 3)

        for p in p_values:
            for d in d_values:
                for q in q_values:
                    try:
                        model = ARIMA(data, order=(p, d, q))
                        results = model.fit()
                        if results.aic < best_aic:
                            best_aic = results.aic
                            best_order = (p, d, q)
                    except:
                        continue
        return best_order

    def fit(self, train_data, order=None):
        if order is None:
            self.order = self.find_best_order(train_data)
        else:
            self.order = order
            
        self.model = ARIMA(train_data, order=self.order)
        self.model_fit = self.model.fit()
        return self.model_fit

    def predict(self, steps):
        return self.model_fit.forecast(steps=steps)

    def evaluate(self, y_true, y_pred):
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        mae = mean_absolute_error(y_true, y_pred)
        mape = mean_absolute_percentage_error(y_true, y_pred)
        return {"RMSE": rmse, "MAE": mae, "MAPE": mape, "Order": self.order}

class GradientBoostingPredictor:
    def __init__(self):
        self.model = GradientBoostingRegressor(random_state=42)

    def fit(self, X_train, y_train):
        param_grid = {
            'n_estimators': [100, 200],
            'learning_rate': [0.01, 0.1],
            'max_depth': [3, 5]
        }
        grid_search = GridSearchCV(self.model, param_grid, cv=3, scoring='neg_mean_squared_error')
        grid_search.fit(X_train, y_train)
        self.model = grid_search.best_estimator_
        return self.model

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, y_true, y_pred):
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        mae = mean_absolute_error(y_true, y_pred)
        mape = mean_absolute_percentage_error(y_true, y_pred)
        return {"RMSE": rmse, "MAE": mae, "MAPE": mape}
