# Task 3: News–Stock Correlation Script

This Python script (`task3_news_stock_correlation.py`) contains reusable functions and logic for analyzing the relationship between news sentiment and stock price movement. It supports the notebook-based analysis in `task3_news_stock_correlation_analysis.ipynb`.
=======
task-2
# Task 2: Modular Stock Analysis Script
---

## Purpose
- Modularize sentiment analysis and stock-news correlation logic.
- Process and clean both news and stock data.
- Calculate sentiment scores and align them with corresponding stock price changes.
- Provide functions to compute and visualize correlations.

---

## Key Features

- Sentiment analysis utilities using tools like VADER or TextBlob.
- Functions for aligning time-series data with news timestamps with stock data.
- Correlation metrics computation using Pearson.
- Designed to support notebook workflows via clean imports.

---

## How to Use

1. Import functions or classes from this script into your notebook or other scripts.
2. Call the appropriate methods to:
   - Load and clean data,
   - Perform sentiment analysis,
   - Compute correlations,
   - Visualize relationships.

---

## Related Notebook

- [`notebooks/task3_news_stock_correlation_analysis.ipynb`](../notebooks/task3_news_stock_correlation_analysis.ipynb)
=======
- Implement modular, reusable code to:
  - Load and prepare stock price data.
  - Calculate technical indicators such as Moving Averages, RSI, and MACD using TA-Lib.
  - Compute financial metrics with PyNance.
  - Support data visualization by preparing processed data.

- Serve as the backend functionality for the analysis performed in the Jupyter Notebook  
  [`notebooks/task2_stock_analysis.ipynb`](../notebooks/task2_stock_analysis.ipynb).

---

## Features

- Functions for data loading and cleaning.
- Classes and methods to calculate various technical indicators.
- Utilities to integrate PyNance financial metrics.
- Designed for easy import and use in notebooks or other Python scripts.

---

## Usage

- Import the module or specific functions/classes into your analysis notebook or script.
- Call the provided functions to process stock data and calculate required indicators.
- Combine with visualization libraries to generate charts reflecting stock behavior.

---

## Dependencies

- [pandas](https://pandas.pydata.org/)
- [TA-Lib](https://mrjbq7.github.io/ta-lib/)
- [PyNance](https://github.com/py-finance/pynance)
- Other standard scientific Python libraries (numpy, matplotlib, etc.)

---

## Related Files

- [`../notebooks/task2_stock_analysis.ipynb`](../notebooks/task2_stock_analysis.ipynb) — Notebook that uses this script for analysis and visualization.
---

**Author:** Mewael Mizan Tesfay  
**GitHub:** [https://github.com/Mewael-EME](https://github.com/Mewael-EME)
=======
=======
# 🗞️ News EDA Script – Week 1 - Task 1

This script performs **Exploratory Data Analysis (EDA)** on news headline data as part of the Week 1 task for the News-Driven Stock Market Analysis Solar Challenge project.

## 📄 Script - `scripts/news_eda.py`

This script includes:
- Reading and inspecting raw news data (CSV)
- Handling missing or null values
- Analyzing headline length, word count, and date distributions
- Visualizing trends and patterns in the news dataset

## 🔧 How to Run

Make sure you have the required dataset (e.g., `news.csv`) in the appropriate folder.

cmd
python scripts/news_eda.py

🛠️ Tools Used
    - Python
    - Pandas
    - Matplotlib
    - Seaborn
