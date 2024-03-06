# ARMA Models for Air Quality Forecasting
- This repository contains code for leveraging ARMA models to forecast air quality, specifically focusing on PM2.5 readings in Nairobi.
# Overview
- ARMA (AutoRegressive Moving Average) models are a class of statistical models widely used for time series analysis and forecasting. 
- In this project, we utilize ARMA models to predict PM2.5 levels in Nairobi, Kenya, based on historical data.
# Key Components
# Data Wrangling
- The data is retrieved from a MongoDB database, where it's preprocessed to remove outliers and resampled for hourly intervals.

# Model Training and Grid Search
- We train ARIMA (AutoRegressive Integrated Moving Average) models with varying parameters (p and q) to find the best fit. We use Mean Absolute Error (MAE) as the criterion for model evaluation.

# Forecasting
- We perform forecasting using ARIMA models on the test dataset, implementing a Walk Forward Validation approach.

# Evaluation and Visualization
- We evaluate model performance using metrics like MAE and visualize the predictions against actual data using line plots and ACF (AutoCorrelation Function) plots.