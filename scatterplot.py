#Scatter plot antara BTC Closing Price dan Sentiment Value tanpa korelasi tertinggi
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
# Load data
df = pd.read_csv("data/Merged_Bitcoin_FearAndGreed.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date').reset_index(drop=True)
# Set window size
window_size = 60
# Membuat scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['BTC_Closing'], df['Value'], alpha=0.7)
plt.title('Scatter Plot BTC Closing vs Value')
plt.xlabel('BTC Closing Price')
plt.ylabel('Sentiment Value')
plt.grid(True)
plt.tight_layout()
plt.show()
