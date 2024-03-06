from ARMAModels.library import plot_pacf, plt
from ARMAModels.y import y

# Create an PACF plot for the data in y
fig, ax = plt.subplots(figsize=(15, 6))
plot_pacf(y, ax=ax)
plt.xlabel("Lag [Hours]")
plt.ylabel("Correlation Coefficient");