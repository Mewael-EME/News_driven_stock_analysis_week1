import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns

class NewsStockCorrelation:
    def __init__(self, news_df, stock_df):
        """
        Initialize the NewsStockCorrelation class with news and stock DataFrames.
        """
        if news_df.empty or stock_df.empty:
            raise ValueError("Input DataFrames cannot be empty.")

        self.news_df = news_df.copy()
        self.stock_df = stock_df.copy()
        self.merged_df = None

    def prepare_data(self):
        """
        Prepare data by parsing dates and merging news and stock datasets.
        """
        # Normalize dates (convert to date only, remove time)
        self.news_df['date'] = pd.to_datetime(self.news_df['date'], errors='coerce').dt.date
        self.stock_df['Date'] = pd.to_datetime(self.stock_df['Date'], errors='coerce').dt.date

        # Aggregate news sentiment per day before merging (average sentiment)
        self.news_df['sentiment_score'] = self.news_df['headline'].apply(
            lambda x: TextBlob(str(x)).sentiment.polarity
        )
        daily_sentiment = self.news_df.groupby('date')['sentiment_score'].mean().reset_index()

        # Merge aggregated daily sentiment with stock data on date
        self.merged_df = pd.merge(daily_sentiment, self.stock_df, left_on='date', right_on='Date', how='inner')

        # Drop rows with missing values in sentiment or Close price
        self.merged_df.dropna(subset=['sentiment_score', 'Close'], inplace=True)

        print("Data Preparation Completed. Merged Data Preview:")
        print(self.merged_df.head())

    def calculate_daily_returns(self):
        """
        Calculate daily percentage change in stock closing prices.
        """
        self.merged_df = self.merged_df.sort_values('Date')
        self.merged_df['Daily_Return'] = self.merged_df['Close'].pct_change()

        # Align sentiment with next day's return (or same day)
        # Option 1: Correlate sentiment today with next day's return
        self.merged_df['Shifted_Sentiment'] = self.merged_df['sentiment_score'].shift(1)

        # Drop NaNs created by pct_change and shift
        self.merged_df.dropna(subset=['Daily_Return', 'Shifted_Sentiment'], inplace=True)

        print("Daily Returns and Shifted Sentiment Calculation Complete.")
        print(self.merged_df[['Date', 'Daily_Return', 'Shifted_Sentiment']].head())

    def analyze_correlation(self):
        """
        Compute Pearson correlation between daily sentiment scores and stock returns.
        """
        analysis_df = self.merged_df.dropna(subset=['Daily_Return', 'Shifted_Sentiment'])

        correlation, p_value = pearsonr(analysis_df['Shifted_Sentiment'], analysis_df['Daily_Return'])

        print("Correlation Analysis Complete.")
        print(f"Pearson Correlation Coefficient: {correlation:.4f}, P-value: {p_value:.4f}")

        return {
            "Correlation_Coefficient": correlation,
            "P_Value": p_value
        }

    def plot_correlation_heatmap(self):
        """
        Plot correlation heatmap of numeric features in the merged dataset.
        """
        if self.merged_df is None or self.merged_df.empty:
            raise ValueError("Merged data is not prepared. Run prepare_data() first.")

        numeric_df = self.merged_df.select_dtypes(include=['number'])

        correlation_matrix = numeric_df.corr()

        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title("Correlation Heatmap of News and Stock Data")
        plt.show()

    def summarize_analysis(self):
        """
        Summarize correlation results and provide insights.
        """
        results = self.analyze_correlation()
        corr = results['Correlation_Coefficient']

        if abs(corr) > 0.5:
            insight = "Strong correlation"
        elif 0.2 < abs(corr) <= 0.5:
            insight = "Moderate correlation"
        else:
            insight = "Weak or no correlation"

        summary = {
            "Correlation_Coefficient": corr,
            "P_Value": results['P_Value'],
            "Insight": insight
        }

        print("\nSummary of Analysis:")
        for k, v in summary.items():
            print(f"{k}: {v}")

        return summary
