import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Veri setini yükle
tweets = pd.read_csv('tweets.csv')

# URL içeren tweetleri ayıkla
url_tweets = tweets[tweets['content'].str.contains(r'http[s]?://\S+')]

# En çok kullanılan ilk 20 URL'i bul
url_counter = Counter(url_tweets['content'].str.extract(r'(http[s]?://\S+)')[0])
top_urls = url_counter.most_common(20)


# URL'ler ve sayılarını ayrı listelere ayır
urls, counts = zip(*top_urls)

print(urls,counts)
# Sonuçları görselleştir
plt.figure(figsize=(12, 8))
sns.barplot(x=counts, y=urls, palette='viridis')
plt.xlabel('URL Sayısı')
plt.ylabel('URL')
plt.title('En Çok Kullanılan İlk 20 URL')
plt.tight_layout()
plt.show()
