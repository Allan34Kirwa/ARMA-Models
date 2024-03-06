from ARMAModels.library import ARIMA, mean_absolute_error,time
from ARMAModels.y import y_train
from ARMAModels.library import pd, sns, plt
# Create ranges for possible  𝑝 and  𝑞 values.
p_params = range(0, 25, 8)
q_params = range(0, 3, 1)

# Convert 'p_params' to a list
list(p_params)

# Convert'q_params' to a list
list(q_params)

# Iterate through parameter combinations, train ARIMA models, and calculate MAE.
# Create empty dictionary for mae values
mae_grid = {}
for p in p_params:
    # Create new key in dictionary with empty list
    mae_grid[p] = []
    for q in q_params:
        # Set the hyperparameters for the model
        order = (p, 0, q)
        # Start timing
        start_time = time.time()
        # Train model
        model = ARIMA(y_train, order=order).fit()
        # Calculate elapsed time
        elapsed_time = round(time.time() - start_time, 2)
        print(f"Trained ARIIMA Model {order} in {elapsed_time}seconds")
        #Generate in sample predictions
        y_pred = model.predict()
        # Calculate MAE
        mae = mean_absolute_error(y_train, y_pred)
        print(mae)
        # Add MAE to our dictionary
        mae_grid[p].append(mae)

# Organize all the MAE's from above in a DataFrame names mae_df
mae_grid
mae_df = pd.DataFrame(mae_grid)
mae_df.round(4)

# Create heatmap of the values in mae_grid
sns.heatmap(mae_df, cmap="Blues")
plt.xlabel("p values")
plt.ylabel("q values")
plt.title("ARMA Grid Search {Criterion: MAE}");

# Use the plot_diagnostics method to check the residuals for your model
fig, ax = plt.subplots(figsize=(15, 12))
model.plot_diagnostics(fig=fig);

