import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns

# Veri setini yükle
df = pd.read_csv('tweets.csv')

# 'date' sütununu tarih formatına dönüştür
df['date'] = pd.to_datetime(df['date'])

# 6 Şubat ile 21 Şubat arasındaki tarih aralığını oluştur
date_range = pd.date_range(start='2023-02-06', end='2023-02-21', freq='D')

# Her gün için tweet sayısını hesapla
tweet_counts = []
for date in date_range:
    count = len(df[df['date'].dt.date == date.date()])
    tweet_counts.append(count)

# Sonuçları DataFrame'e dönüştür
result_df = pd.DataFrame({
    'Date': date_range,
    'Tweet Count': tweet_counts
})

# Çizgi grafiğini çiz
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
plt.plot(result_df['Date'], result_df['Tweet Count'], linestyle='-', linewidth=2, alpha=0.7, color='b')


# Logaritmik ölçek kullan
plt.yscale('log')

# ScalarFormatter kullanarak y ekseni etiketlerini normal sayılar olarak ayarla
plt.gca().yaxis.set_major_formatter(ScalarFormatter())

# X eksenini günlerin her biri olacak şekilde ayarla
plt.xticks(date_range, [date.strftime('%Y-%m-%d') for date in date_range], rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Günlük Tweet Sayıları (06 Şubat - 21 Şubat 2023)', fontsize=14)
plt.xlabel('Tarih', fontsize=12)
plt.ylabel('Tweet Sayısı (log ölçeği)', fontsize=12)
plt.tight_layout()

# Grafik göstermek
plt.show()
