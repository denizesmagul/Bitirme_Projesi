import pandas as pd
import matplotlib.pyplot as plt
import re
import seaborn as sns

# Veri setini yükle
tweets = pd.read_csv('tweets.csv')

# Tarih kolonunu datetime formatına çevir
tweets['date'] = pd.to_datetime(tweets['date'])

# 6-21 Şubat arasındaki tweetleri filtrele
start_date = '2023-02-06'
end_date = '2023-02-21'
filtered_tweets = tweets[(tweets['date'] >= start_date) & (tweets['date'] <= end_date)]

# URL içeren tweetleri saymak için bir fonksiyon
def count_urls(text):
    url_pattern = re.compile(r'http[s]?://\S+')
    return len(url_pattern.findall(text)) > 0

# Her gün için URL içeren tweet sayısını hesapla
filtered_tweets['has_url'] = filtered_tweets['content'].apply(count_urls)
daily_url_counts = filtered_tweets.groupby(filtered_tweets['date'].dt.date)['has_url'].sum()

# URL içeren ve içermeyen tweetlerin toplamını hesapla
total_tweets = len(filtered_tweets)
tweets_with_urls = filtered_tweets['has_url'].sum()
tweets_without_urls = total_tweets - tweets_with_urls

# Konsola yazdır
print(f"Toplam tweet sayısı: {total_tweets}")
print(f"URL içeren tweet sayısı: {tweets_with_urls}")
print(f"URL içermeyen tweet sayısı: {tweets_without_urls}")

# Sonuçları görselleştir
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
daily_url_counts.plot(kind='bar', color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Tarih')
plt.ylabel('Tweet Sayısı')
plt.title('URL İçerikli Tweetlerin Günlük Yoğunluğu (06 Şubat - 21 Şubat 2023)')
plt.tight_layout()
plt.show()
