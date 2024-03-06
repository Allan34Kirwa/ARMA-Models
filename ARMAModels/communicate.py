from ARMAModels.library import pd, px
from ARMAModels.y import y_test
from ARMAModels.evaluation import y_pred_wfv

# Generate in-sample predictions with statsmodels, create DataFrame from dict using pandas, plot using pandas line plot
df_predictions = pd.DataFrame({"y_test": y_test, "y_pred_wfv": y_pred_wfv})
fig = px.line(df_predictions, labels={"value":"PM2.5"})
fig.show()