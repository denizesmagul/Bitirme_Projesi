import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

#Veri setini yükle
tweets = pd.read_csv('tweets.csv')

#Hastag'leri küçük harfe çevirme fonksiyonu
def lowercase_hashtags(tags_list):
    if pd.notnull(tags_list):
        tags = eval(tags_list)
        return [tag.lower() for tag in tags]
    else:
        return []


#Hashtag'leri küçük harfe çevir
tweets['hashtags'] = tweets['hashtags'].apply(lowercase_hashtags)


##Toplam tweet sayısını hesapla
total_tweet_count = len(tweets)
print(f"Toplam tweet sayısı: {total_tweet_count}")

#Hashtag kolonu boş olan tweetlerin sayısını hesapla
empty_hashtags_count = tweets['hashtags'].apply(lambda x: len(x) == 0).sum()
print(f"Hashtag kolonu boş olan tweet sayısı: {empty_hashtags_count}")

#Tüm hashtag'leri birleştir ve başlarına # işareti ekle
all_hashtags = [f'#{tag}' for sublist in tweets['hashtags'] for tag in sublist]


#En çok kullanılan hashtag'leri ve kullanım sayılarını bul
top_hashtags = pd.Series(all_hashtags).value_counts().head(10)


print("En Çok Kullanılan 10 Hashtag ve Kullanım Sayıları:")
for hashtag, count in top_hashtags.items():
    print(f"{hashtag}: {count}")

#ubuk grafiği oluştur
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
plt.bar(top_hashtags.index, top_hashtags.values, color='skyblue')

plt.xticks(rotation=45, ha='right')
plt.ylabel('Kullanım Sayısı')
plt.xlabel('Hashtagler')
plt.title('En Fazla Kullanılan 10 Hashtag')


plt.tight_layout()
plt.show()
hashtag_counts = Counter(all_hashtags)
filtered_hashtags = {k: v for k, v in hashtag_counts.items() if v >= 2000}

# WordCloud oluştur
wordcloud = WordCloud(width=800, height=400, background_color='black').generate_from_frequencies(hashtag_counts)

# WordCloud'u göster
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Hashtag WordCloud')
plt.show()