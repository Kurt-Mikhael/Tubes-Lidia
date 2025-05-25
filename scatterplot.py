#Menghitung korelasi antara 'Value' dan 'BTC_Closing' setiap tahun
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta
# Load the dataset
df = pd.read_csv("data/Merged_Bitcoin_FearAndGreed.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date').reset_index(drop=True)
# Set the window size
window_size = 60

#MEnghitung korelasi untuk setiap tahun
yearly_corr = df.groupby(df['Date'].dt.year).apply(
    lambda x: x['Value'].corr(x['BTC_Closing'])
).reset_index(name='Correlation')
# Plotting the yearly correlation
plt.figure(figsize=(12, 6))
sns.barplot(x='Date', y='Correlation', data=yearly_corr, palette='viridis')
plt.title('Yearly Correlation between Sentiment BTC Closing and Change')
plt.xlabel('Year')
plt.ylabel('Correlation Coefficient')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Print the yearly correlation results
print("=== Yearly Correlation Results ===")
print(yearly_corr.to_string(index=False))

#Korelasi dengan dengan semua rentang waktu
all_corr = df['Value'].corr(df['BTC_Closing'])
print(f"\nOverall Correlation between Sentiment and BTC Closing: {all_corr:.4f}")
# Plotting the overall correlation
plt.figure(figsize=(8, 6))
plt.scatter(df['Value'], df['BTC_Closing'], alpha=0.7)
plt.title('Scatter Plot of Sentiment vs BTC Closing')
plt.xlabel('Sentiment')
plt.ylabel('BTC Closing Price')
plt.grid(True)
plt.tight_layout()
plt.show()


