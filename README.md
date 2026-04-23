# Reliance-Industries-Stock-Forecast-
Forecasting stock prices of Reliance Industries Limited using ML &amp; time series models (ARIMA, SARIMA, LSTM, Linear Regression, Random Forest). Analyzes 2000–2023 data, captures trends, and predicts future prices. Includes EDA, model comparison, and Streamlit deployment for interactive forecasting.

This project focuses on forecasting the stock prices of Reliance Industries Limited using a combination of statistical, machine learning, and deep learning models. It demonstrates a complete end-to-end data science pipeline—from data collection to deployment.

🎯 Business Objective

The primary objective of this project is to:

Predict Reliance stock prices for the next 1 year
Analyze short-term and long-term trends
Understand the impact of external market factors and events
Build a robust forecasting model using historical data (2000–2023)

📁 Dataset

Source: NSE historical data (RELIANCE.NS)

Time Period: 2000 – 2023

Records: ~6,079 trading days

Features:

Open

High

Low

Close (Target Variable)

Volume

🔍 Problem Statement

Stock prices are:

Highly volatile

Non-stationary in nature

Strongly dependent on past values (temporal dependency)

This project addresses these challenges using advanced time series and ML models to improve prediction accuracy.

⚙️ Project Workflow

Data Collection & Cleaning

Exploratory Data Analysis (EDA)

Feature Engineering (Moving Averages, Lag Features)

Model Building

Model Evaluation (RMSE)

Deployment using Streamlit

🤖 Models Implemented

ARIMA

SARIMA

Linear Regression (Lag-based)

Random Forest

LSTM (Deep Learning)


📊 Results & Performance

Model	RMSE (INR)	Rank

Linear Regression	29.98	🥇 Best

Random Forest	188.37	🥈

SARIMA	385.54	🥉

ARIMA	443.83	4th

🔑 Key Insights

Linear Regression performed best due to strong autocorrelation

SARIMA captured seasonality effectively

LSTM showed learning capability but needs more tuning

SARIMA was selected for deployment due to multi-step forecasting capability

🚀 Deployment

Model saved using Pickle (.pkl)

Interactive web app built using Streamlit

Enables users to visualize and forecast stock prices

🛠️ Technologies Used

Programming & Libraries

Python

Pandas, NumPy

Matplotlib, Seaborn

Machine Learning

Scikit-learn

Statsmodels

TensorFlow / Keras

Tools

Jupyter Notebook

Streamlit

GitHub

⏳ Project Timeline

Total Duration: 30 Days

Data Analysis, Model Building, Evaluation, and Deployment phases included

📈 Key Achievements

Built an end-to-end ML pipeline

Compared 5 different models

Achieved high accuracy with minimal features

Successfully deployed a forecasting application

🔮 Future Scope

Add technical indicators (RSI, MACD, Bollinger Bands)

Use advanced models like GRU & Transformers

Integrate real-time APIs (NSE/Yahoo Finance)

Deploy on cloud (AWS/GCP)

Build multi-stock prediction dashboard

📌 Conclusion

This project demonstrates how different modeling approaches—statistical, machine learning, and deep learning—can be applied to financial time series forecasting. It highlights the importance of model selection, feature engineering, and proper evaluation in building reliable prediction systems.

⭐ Project Highlights
📊 Time Series Forecasting
🤖 Machine Learning + Deep Learning
📈 Financial Data Analysis
🚀 Deployment with Streamlit
