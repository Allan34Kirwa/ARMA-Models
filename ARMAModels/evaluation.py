from ARMAModels.library import pd, ARIMA, mean_absolute_error
from ARMAModels.y import y_train, y_test

# Perform ARIMA forecasting on y_train data iteratively to predict y_test values
y_pred_wfv = pd.Series()
history = y_train.copy()
for i in range(len(y_test)):
    model = ARIMA(history, order=(8, 0, 1)).fit()
    next_pred = model.forecast()
    y_pred_wfv = y_pred_wfv.append(next_pred)
    history = history.append(y_test[next_pred.index])

# Calculate and print the test Mean Absolute Error (MAE) for walk forward validation.
test_mae = mean_absolute_error(y_test, y_pred_wfv)
print("Test MAE (walk forward validation):", round(test_mae, 2))