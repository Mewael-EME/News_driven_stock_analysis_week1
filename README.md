# 📰📈 News-Driven Stock Market Analysis – Week 1 - Task 1

Welcome to Week 1 : *News-Driven Stock Market Analysis*.  
This repository initiates the exploration of how news data and stock market trends can be analyzed for potential insights using Python.

---

## 📁 Project Structure
```
News_driven_stock_analysis_week1/
│
├── .vscode/
│ └── settings.json
│
├── .github/
│ └── workflows/
│ └── unittests.yml
│
├── .gitignore
│
├── requirements.txt
│
├── README.md
│
├── src/
│ └── init.py
│
├── notebooks/
│ ├── init.py
│ └── README.md
│
├── tests/
│ └── init.py
│
└── scripts/
├── init.py
└── README.md
```

## 📓 Main Components

### ✅ `notebooks/stock_market_analysis.ipynb`
- Loads and preprocesses stock data
- Performs exploratory data analysis (EDA)
- Visualizes trends and statistics using plots

### ✅ `scripts/news_eda.py`
- Reads news headline datasets
- Cleans and analyzes textual data
- Visualizes word distributions, lengths, and temporal patterns

---

## 🔧 How to Use

1. **Clone the repository:**
   ```cmd
   git clone https://github.com/Mewael-EME/News_driven_stock_analysis_week1.git
   cd News_driven_stock_analysis_week1

2. Run the notebook:
   cmd : jupyter notebook notebooks/stock_market_analysis.ipynb

3. Run the script:
  cmd: python scripts/news_eda.py

🛠️ Tools & Libraries
  - Python
  - Pandas
  - Matplotlib & Seaborn
  - Jupyter Notebook

Made by Mewael Mizan Tesfay
=======
# 📰📈 News Driven Stock Analysis – Week 1

This repository is part of a multi-stage project focused on analyzing how financial news affects stock price behavior. Using Python, finance APIs, sentiment analysis tools, and visualization libraries, the project evolves across tasks — from technical stock analysis to correlating news sentiment with market movement.

---

## ✅ Weekly Breakdown

### 🔹 Task 1: Stock Data Loading & Visualization
- Load historical stock price data.
- Visualize Open, High, Low, Close, and Volume.
- Basic moving averages (SMA/EMA).

📁 Notebook: `notebooks/task1_stock_data_analysis.ipynb`  
📁 Scripts: `scripts/task1_stock_functions.py`

---

### 🔹 Task 2: Technical Indicator Analysis
- Apply **TA-Lib** to compute:
  - Moving Averages
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
- Use **PyNance** for advanced metrics.
- Modularize code into reusable functions and classes.

📁 Notebook: `notebooks/task2_stock_analysis.ipynb`  
📁 Scripts: `scripts/task2_stock_analysis.py`

---

### 🔹 Task 3: News Sentiment & Stock Correlation
- Scrape or load financial news headlines.
- Apply **sentiment analysis** (e.g., VADER/TextBlob).
- Synchronize sentiment with stock data.
- Compute correlation coefficients (Pearson, Spearman).
- Visualize insights.

📁 Notebook: `notebooks/task3_news_stock_correlation_analysis.ipynb`  
📁 Scripts: `scripts/task3_news_stock_correlation.py`

---

## 🗂️ Project Structure
```
/
├── notebooks/ # Jupyter notebooks for each task
├── scripts/ # Python modules with reusable functions and classes
├── data/ # Raw or cleaned stock/news data (if available)
├── README.md # Project overview
└── requirements.txt # List of dependencies
```


---

## 🧪 Tech Stack

- **Python** (Pandas, Numpy, Matplotlib, Seaborn)
- **TA-Lib** (Technical indicators)
- **PyNance** (Finance analytics)
- **NLTK / VADER / TextBlob** (Sentiment Analysis)
- **Jupyter Notebooks**
- **Git** (branching, PRs, version control)

---

## 🔑 Key Learning Outcomes

- Hands-on stock market data analysis
- Sentiment impact on financial data
- Use of indicators for market prediction
- Modular, reusable, and scalable code practices
- Clear GitHub-based collaboration with commits, branches, and PRs

---

## 👤 Author

**Mewael Mizan Tesfay**  
[GitHub](https://github.com/Mewael-EME)

---
