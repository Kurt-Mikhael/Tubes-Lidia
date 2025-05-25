import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/Merged_Bitcoin_FearAndGreed.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date').reset_index(drop=True)

# Setting 
window_size = 60
best_corr = -1
best_span = (None, None)
best_df = None




# Mencari Rentang Waktu dengan Korelasi Tertinggi
for i in range(len(df) - window_size + 1):
    sub_df = df.iloc[i:i+window_size]
    corr = sub_df['Value'].corr(sub_df['Change'])
    if pd.notna(corr) and corr > best_corr:
        best_corr = corr
        best_span = (sub_df['Date'].iloc[0], sub_df['Date'].iloc[-1])
        best_df = sub_df.copy()


# Menambahkan 10 Hari Sebelum dan Sesudah Rentang Terbaik (Untuk pemenuhan tugas)
extra_days = 10
extended_start = best_span[0] - pd.Timedelta(days=extra_days)
extended_end = best_span[1] + pd.Timedelta(days=extra_days)
extended_df = df[(df['Date'] >= extended_start) & (df['Date'] <= extended_end)].copy()

# Menghitung Korelasi pada Data Diperluas
extended_corr = extended_df['Value'].corr(extended_df['Change'])

plt.figure(figsize=(12, 6))
plt.scatter(extended_df['Value'], extended_df['Change'], alpha=0.7)
plt.title(f'Scatter Plot Change vs Value\n(Extended: {extended_start.date()} to {extended_end.date()})')
plt.xlabel('Sentiment')
plt.ylabel('Change')
plt.grid(True)
plt.tight_layout()
plt.show()

# Print
print("=== Hasil Korelasi Diperluas ===")
print(f"Rentang Tanggal : {extended_start.date()} sampai {extended_end.date()}")
print(f"Jumlah Data     : {len(extended_df)} hari")
print(f"Koefisien Korelasi : {extended_corr:.4f}")
