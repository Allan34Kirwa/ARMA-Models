from ARMAModels.y import y

# Overview of my series data
y.head()

# Create a training set y_train (only readings from October 2018), & a test set y_test that contains readings from November 1, 2018
y_train = y['2018-10']
y_test = y['2018-11-01']

# Display the first 3 rows of the y_train dataset.
y_train.head(3)

# Displaying the first 3 rows of the y_test dataset.
y_test.head(3)