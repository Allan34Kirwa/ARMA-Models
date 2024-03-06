from ARMAModels.splitdata import y_train
from ARMAModels.library import mean_absolute_error

# Calculate the mean of the training labels and use it as a baseline prediction.
# Compute the Mean Absolute Error (MAE) for the baseline prediction.
y_train_mean = y_train.mean()    # Mean of training labels
y_pred_baseline = [y_train_mean] * len(y_train)  # Baseline prediction
mae_baseline = mean_absolute_error(y_train, y_pred_baseline)  # Baseline MAE
print("Mean P2 Reading:", round(y_train_mean, 2))  # Print mean P2 reading
print("Baseline MAE:", round(mae_baseline, 2))  # Print baseline MAE