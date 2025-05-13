# Bitcoin Price Analysis with Fear and Greed Index

This project analyzes Bitcoin price data in relation to market sentiment using the Fear and Greed Index. The analysis includes data preprocessing, statistical analysis, and visualizations to explore trends and relationships between Bitcoin prices and market sentiment.

---

## Project Structure

```
Tubes-Lidia/
├── data
│   ├── BTC_FearAndGreed.csv            # Fear and Greed index dataset
│   ├── Bitcoin_History.csv             # Raw Bitcoin historical price dataset
│   ├── Bitcoin_History_Updated.csv     # Cleaned and transformed Bitcoin price dataset
│   └── Merged_Bitcoin_FearAndGreed.csv # Combined dataset of Bitcoin price and Fear and Greed Index
├── README.md                           # Project documentation
├── Statistika-Deskriptif.ipynb         # Notebook for descriptive statistics and analysis
├── Visualisasi-Data.ipynb              # Notebook for data visualization
```

---

## Datasets

### 1. **Bitcoin_History.csv**

- Contains raw historical Bitcoin price data, including:
  - Open, High, Low, Close prices
  - Volume
  - Percentage change (`Change %`)

### 2. **BTC_FearAndGreed.csv**

- Time series data of the Fear and Greed Index, representing market sentiment.

### 3. **Bitcoin_History_Updated.csv**

- Cleaned and transformed version of `Bitcoin_History.csv`:
  - Converted `Change %` to a float format.
  - Added a `Change Classification` column to categorize price changes as `Up`, `Down`, or `Stable`.

### 4. **Merged_Bitcoin_FearAndGreed.csv**

- Combined dataset of Bitcoin price data and Fear and Greed Index:
  - Merged on the `Date` column.
  - Includes additional sentiment classifications (`Value_Classification`).

---

## Analysis Overview

### 1. **Data Preparation**

- Cleaning and transforming raw data:
  - Removing unnecessary columns (e.g., `Vol.`).
  - Handling missing values using forward fill.
  - Converting data types for numerical and date columns.
  - Merging datasets for combined analysis.

### 2. **Descriptive Statistics**

- Calculated key metrics for numerical attributes (`Open`, `Close`, `High`, `Low`, `Change`, `BTC_Volume`, `Value`):
  - Mean, Median, Standard Deviation
  - Percentiles (10th, 25th, 50th, 75th, 90th)
- Frequency distributions for numerical attributes.

### 3. **Categorical Data Analysis**

- Distribution of `Change Classification` (Up, Down, Stable).
- Distribution of `Value_Classification` (Extreme Fear, Fear, Neutral, Greed, Extreme Greed).

### 4. **Visualizations**

- Line plots for price trends (`Open`, `Close`, `High`, `Low`) over time.
- Scatter plots for Bitcoin closing price vs sentiment categories.
- Histograms for frequency distributions of numerical attributes.
- Pie charts for categorical data distributions.

---

## Notebooks

### 1. **Statistika-Deskriptif.ipynb**

- Focuses on descriptive statistics for Bitcoin price data.
- Includes calculations for key metrics and frequency distributions.
- Saves cleaned and processed data to CSV files.

### 2. **Visualisasi-Data.ipynb**

- Creates visualizations to explore trends and relationships in the data.
- Includes:
  - Line plots for price trends.
  - Scatter plots for sentiment analysis.
  - Pie charts for categorical distributions.

---

## How to Run the Project

### Prerequisites

- Python 3.x
- Jupyter Notebook or JupyterLab
- Required Python libraries:
  - `pandas`
  - `matplotlib`
  - `numpy`
  - `seaborn`
  - `scipy`

### Installation

1. Clone or download this repository to your local machine.

2. Install the required Python packages:

   ```bash
   pip install pandas matplotlib numpy seaborn scipy jupyter
   ```

3. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

4. Open and run the notebooks:
   - `Statistika-Deskriptif.ipynb` for data cleaning and descriptive statistics.
   - `Visualisasi-Data.ipynb` for data visualization.

---

## Key Insights

- The Fear and Greed Index provides valuable insights into market sentiment and its relationship with Bitcoin price movements.
- Statistical analysis reveals trends and patterns in Bitcoin price data over time.
- Visualizations help identify correlations between sentiment and price attributes.

---

## Authors

| NIM      | Nama                            |
| -------- | ------------------------------- |
| 13524001 | Samuelson Dharmawan Tanuraharja |
| 13524027 | Aufa Rienaldifaza Ahmad         |
| 13524037 | Nicholas Wise Saragih Sumbayak  |
| 13524065 | Kurt Mikhael Purba              |
| 13524069 | Miguel Rangga Deardo Sinaga     |
