import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

def set_plot_style():
    # Set seaborn style
    sns.set(style="whitegrid")
    
    # Set plot size
    plt.figure(figsize=(8, 8))

def plot_stock_prices(df):
    set_plot_style()
    
    # Plot the closing prices
    sns.lineplot(x=df.index, y='Close', data=df, label='Closing Price', color='blue')
    
    plt.title('Stock Closing Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.show()

def plot_time_series_decomposition(df, period):
    set_plot_style()

    num_observations = len(df)
    if num_observations < 2 * period:
        period = num_observations // 2

   
    result = seasonal_decompose(df['Close'], model='additive', period=period)

    plt.subplot(4, 1, 1)
    plt.title("Time Series Plot of Closing Prices")
    sns.lineplot(x=df.index, y=result.observed, label='Observed', color='blue')
    plt.legend()

    plt.subplot(4, 1, 2)
    plt.title("Trend Analysis")
    sns.lineplot(x=df.index, y=result.trend, label='Trend', color='green')
    plt.legend()

    plt.subplot(4, 1, 3)
    plt.title("Seasonal Analysis")
    sns.lineplot(x=df.index, y=result.seasonal, label='Seasonal', color='red')
    plt.legend()

    plt.subplot(4, 1, 4)
    plt.title("Residual Analysis")
    sns.lineplot(x=df.index, y=result.resid, label='Residual', color='purple')
    plt.legend()

    plt.tight_layout()
    plt.show()
