import pandas as pd
import matplotlib.pyplot as plt
import talib
import pynance as pn

class StockAnalysis:
    def __init__(self, dataframe):
        """
        Initialize the StockAnalysis class with a pandas DataFrame.

        Parameters:
        dataframe (pd.DataFrame): Stock data with columns ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        """
        self.df = dataframe

    def prepare_data(self):
        """
        Ensure data is correctly formatted and check for required columns.
        
        Returns:
        pd.DataFrame: Prepared DataFrame with 'Date' as index.
        
        Raises:
        ValueError: If required columns are missing.
        """
        required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        if not all(col in self.df.columns for col in required_columns):
            raise ValueError(f"DataFrame must include the following columns: {required_columns}")
        
        # Ensure 'Date' is datetime and set as index
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df.set_index('Date', inplace=True)
        
        return self.df.head()

    def calculate_technical_indicators(self):
        """
        Calculate common technical indicators using TA-Lib and add them to the DataFrame.

        Returns:
        pd.DataFrame: DataFrame with new columns for SMA_20, EMA_20, RSI, MACD, MACD_signal, MACD_hist
        """
        # Moving Averages
        self.df['SMA_20'] = talib.SMA(self.df['Close'], timeperiod=20)
        self.df['EMA_20'] = talib.EMA(self.df['Close'], timeperiod=20)

        # Relative Strength Index (RSI)
        self.df['RSI'] = talib.RSI(self.df['Close'], timeperiod=14)

        # Moving Average Convergence Divergence (MACD)
        macd, macd_signal, macd_hist = talib.MACD(
            self.df['Close'], fastperiod=12, slowperiod=26, signalperiod=9
        )
        self.df['MACD'] = macd
        self.df['MACD_signal'] = macd_signal
        self.df['MACD_hist'] = macd_hist

        return self.df[['SMA_20', 'EMA_20', 'RSI', 'MACD', 'MACD_signal', 'MACD_hist']].head()

    def calculate_financial_metrics(self):
        """
        Calculate additional financial metrics using PyNance or basic pandas.

        Returns:
        pd.DataFrame: DataFrame with 'Daily_Return' and 'Volatility' columns.
        """
        # Daily returns
        self.df['Daily_Return'] = self.df['Close'].pct_change()

        # Rolling volatility (std dev of returns)
        self.df['Volatility'] = self.df['Daily_Return'].rolling(window=20).std()

        return self.df[['Daily_Return', 'Volatility']].head()

    def visualize_data(self):
        """
        Create visualizations for stock prices and technical indicators.
        """
        # Plot Close Price with Moving Averages
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['Close'], label='Close Price', color='blue')
        plt.plot(self.df['SMA_20'], label='20-day SMA', color='red', linestyle='--')
        plt.plot(self.df['EMA_20'], label='20-day EMA', color='green', linestyle='--')
        plt.title('Stock Price with Moving Averages')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

        # Plot RSI with thresholds
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['RSI'], label='RSI', color='purple')
        plt.axhline(70, color='red', linestyle='--', label='Overbought')
        plt.axhline(30, color='green', linestyle='--', label='Oversold')
        plt.title('Relative Strength Index (RSI)')
        plt.xlabel('Date')
        plt.ylabel('RSI Value')
        plt.legend()
        plt.show()

        # Plot MACD
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['MACD'], label='MACD', color='blue')
        plt.plot(self.df['MACD_signal'], label='Signal Line', color='orange')
        plt.bar(self.df.index, self.df['MACD_hist'], label='Histogram', color='gray', alpha=0.5)
        plt.title('MACD')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        plt.show()

    def validate_indicators(self):
        """
        Check for missing values in the calculated indicators.

        Returns:
        pd.Series: Count of missing values in each column where missing values exist.
        """
        missing_data = self.df.isnull().sum()
        return missing_data[missing_data > 0]
