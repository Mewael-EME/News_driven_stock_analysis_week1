task-2
# Task 2: Modular Stock Analysis Script

This Python script (`task2_stock_analysis.py`) contains the core **functions and classes** used for quantitative stock analysis in **Week 1, Task 2** of the News Driven Stock Analysis project.

---

## Purpose

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

