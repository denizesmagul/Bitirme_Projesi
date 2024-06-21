import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Tweet verilerini yükle
tweets = pd.read_csv('tweets.csv')

# 6 Şubat depreminde etkilenen illerin listesi
cities = ["Adana", "Gaziantep", "Malatya", "Adıyaman", "Kahramanmaraş", "Diyarbakır", "Hatay", "Elazığ", "Osmaniye", "Kilis", "Şanlıurfa"]

# Tweetlerdeki il isimlerini saymak için Counter oluştur
city_counts = Counter()

# Tweetler içerisindeki il isimlerini bul
for tweet in tweets['content']:
    for city in cities:
        if city.lower() in tweet.lower():
            city_counts[city] += 1

# Grafik için verileri hazırla
cities = list(city_counts.keys())
counts = list(city_counts.values())
import seaborn as sns
# Bar grafik oluştur
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
plt.bar(cities, counts, color='skyblue')

# Eksen ve başlık etiketlerini ayarla
plt.xlabel('İller', fontsize=12)
plt.ylabel('Tweet Sayısı', fontsize=12)
plt.title('İl İçerikli Tweet Sayısı', fontsize=14)

# Eksen etiketlerini döndür
plt.xticks(rotation=45, ha='right', fontsize=10)

# Grafik göster
plt.tight_layout()
plt.show()


