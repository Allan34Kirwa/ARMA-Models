from ARMAModels.library import plt, plot_acf
from ARMAModels.y import y

# Create an ACF plot for the data in y
fig, ax = plt.subplots(figsize=(15, 6))
plot_acf(y, ax=ax)
plt.xlabel("Lag [Hours]")
plt.ylabel("Correlation Coefficient");