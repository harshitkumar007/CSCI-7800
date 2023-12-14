# CSCI-7850 - Stock Price Prediction Project

This project employs deep learning techniques, specifically Gated Recurrent Unit (GRU) models, to predict Google's stock prices based on historical market data. 
It includes Jupyter Notebooks, Python scripts, and datasets used for model training and evaluation.

## Introduction

This repository explores machine learning models, particularly GRU models, for accurate stock price prediction based on historical data. By leveraging deep learning techniques, the project aims to provide insights into Google's stock price trends.

## Dataset
This project utilizes historical stock market data for Google to train and evaluate the predictive models. 
The dataset includes both training and test data in CSV format.

Google Stock Data
Google_Stocks_Train.csv: Contains historical training data for Google stock prices.
Google_Stocks_Test.csv: Consists of test data for Google stock prices.
The data comprises various features and labels necessary for training and evaluating the predictive models.
## Files

- **GRU.ipynb**: Jupyter Notebook containing code for implementing, training, and evaluating GRU models for stock price prediction.
- **Google_Stocks_Test.csv**: CSV file with test data for Google stock prices.
- **Google_Stocks_Train.csv**: CSV file containing training data for Google stock prices.
- **Plots.py**: Python script with functions for generating various plots and visualizations related to stock price analysis.
- **Stock.py**: Python script containing functions and classes for stock data processing and analysis.
- **requirements.txt**: File listing all required dependencies and their versions for running the code.
- **train_loss.csv**: CSV file recording training loss values during model training.
- **val_loss.csv**: CSV file recording validation loss values during model training.

## Project Structure

The project directory is organized as follows:

```
stock_market_prediction/
│
├── GRU/
│   ├── GRU.ipynb
│   ├── Plots.py
│   ├── Stock.py
│   ├── Google_Stocks_Train.csv
│   └── Google_Stocks_Test.csv
├── train_loss.csv
└── val_loss.csv
```

## Data Description

Both `Google_Stocks_Train.csv` and `Google_Stocks_Test.csv` contain historical stock data for Google. Columns include 'Date', 'Open', 'High', 'Low', 'Close', 'Volume', and 'Adj Close'. The 'Adj Close' column was removed during preprocessing.

## Methodology

The GRU (Gated Recurrent Unit) model used in `GRU.ipynb` is a type of recurrent neural network (RNN) specialized for sequence modeling tasks. GRU's ability to retain long-term dependencies makes it suitable for time-series forecasting tasks like stock price prediction.

## Results

The project achieved promising results in stock price prediction accuracy, with the GRU model demonstrating robustness in capturing complex temporal patterns.

## Usage

To reproduce the analysis or run the code:

1. Clone this repository: `git clone https://github.com/harshitkumar007/CSCI-7800.git`
2. Navigate to the project directory.
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the `GRU.ipynb` notebook to train and evaluate the GRU models.
5. Utilize `Plots.py` and `Stock.py` scripts for additional analysis and visualization.

Note: Ensure Python and Jupyter Notebook are installed on your system.

## Future Improvements

Potential enhancements include experimenting with different deep learning architectures, exploring additional features, and fine-tuning hyperparameters to improve model accuracy further.

