# Bitcoin Price Analysis with Fear and Greed Index

This project analyzes Bitcoin price data in relation to market sentiment using the Fear and Greed Index. The analysis includes statistical measurements, data visualization, and frequency distributions of various price attributes.

## Project Structure

```
Tubes-Lidia/
├── TubesLidia.ipynb       # Main Jupyter notebook containing all analysis
├── README.md              # This file
└── File/                  # Data directory
    ├── Bitcoin_History.csv              # Original Bitcoin historical price data
    ├── Bitcoin_History_Updated.csv      # Processed Bitcoin data with additional features
    ├── BTC_FearAndGreed.csv            # Fear and Greed Index data
    └── Merged_Bitcoin_FearAndGreed.csv  # Combined dataset for analysis
```

## Dataset Description

- **Bitcoin_History.csv**: Raw historical price data for Bitcoin including Open, High, Low, Close prices, and volume.
- **BTC_FearAndGreed.csv**: Time series data of the Fear and Greed Index for Bitcoin, representing market sentiment.
- **Merged_Bitcoin_FearAndGreed.csv**: Combined dataset with both price data and sentiment indicators.

## Analysis Performed

The notebook performs comprehensive statistical analysis and visualization on Bitcoin price data:

1. **Data Preparation**
   - Converting data types
   - Handling missing values
   - Feature engineering (adding Change Classification)
   - Merging price data with Fear and Greed Index data

2. **Statistical Analysis** for each key attribute (Open, Close, High, Low, Change, BTC_Volume, Value):
   - Descriptive statistics (mean, median, standard deviation)
   - Percentile calculations (10th, 25th, 50th, 75th, 90th)
   - Frequency distributions with visualizations

3. **Categorical Data Analysis**
   - Distribution of Change Classification (Up, Down, Stable)
   - Distribution of Fear and Greed Index classifications

4. **Visualizations**
   - Histograms for numerical attributes
   - Pie charts for categorical data
   - Statistical markers on visualizations (mean, median, percentiles)

## How to Run the Project

### Prerequisites
- Python 3.x
- Jupyter Notebook/JupyterLab
- Required Python libraries: pandas, matplotlib, numpy, scipy

### Installation

1. Clone or download this repository to your local machine.

2. Install the required Python packages:
```
pip install pandas matplotlib numpy scipy jupyter
```

3. Launch Jupyter Notebook:
```
jupyter notebook
```

4. Navigate to and open the `TubesLidia.ipynb` file.

5. Run all cells in the notebook by clicking "Run All" or execute each cell sequentially.

### Expected Output

The notebook will:
- Load and process the Bitcoin historical data and Fear and Greed Index data
- Generate statistical summaries for all key attributes
- Create visualizations showing distributions and key metrics
- Save processed data to CSV files in the File directory

## Notes

- The analysis focuses on understanding the statistical properties of Bitcoin price movements.
- The Fear and Greed Index is used as a sentiment indicator for the cryptocurrency market.
- Change Classification categorizes price movements as Up, Down, or Stable based on percentage changes.

---

Created for Data Science Project Analysis
