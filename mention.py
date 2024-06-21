import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# tweets.csv dosyasını okuma
df = pd.read_csv('tweets.csv')


# Mention'ları bulmak için regex deseni
mention_pattern = re.compile(r'@(\w+)')


# Mention'ları saklamak için Counter
mention_counter = Counter()

# Content kolonundaki tweet'lerde mention'ları bulma
for tweet in df['content']:
    # Her tweet'teki tüm mention'ları bul
    mentions = mention_pattern.findall(tweet)
    # Mention'ları mention_counter'a ekle
    mention_counter.update(mentions)

# Mention'ların başına @ işareti ekleme
mention_counter = Counter({'@' + mention: count for mention, count in mention_counter.items()})


# En çok kullanılan mention'ları bulma
most_common_mentions = mention_counter.most_common(10)  # En çok kullanılan 10 mention

# En çok kullanılan mention'ları konsola yazdırma
print("En Çok Kullanılan 10 Mention ve Kullanım Sayıları:")
for mention, count in most_common_mentions:
    print(f"{mention}: {count}")

# En çok kullanılan mention'ları DataFrame'e dönüştürme
mention_df = pd.DataFrame(most_common_mentions, columns=['mention', 'count'])

# Content kolonundaki tweet'lerde @ kullanıcı adı olmayan tweetlerin sayısını bulma
tweets_without_mentions_count = df['content'].apply(lambda x: len(mention_pattern.findall(x)) == 0).sum()
print(f"Veri setindeki @ kullanıcı adı olmayan tweet sayısı: {tweets_without_mentions_count}")

# Çubuk grafiği oluşturma
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
plt.bar(mention_df['mention'], mention_df['count'], color='skyblue')

# Grafiği biçimlendirme
plt.xticks(rotation=45, ha='right')
plt.xlabel('Mentionlar')
plt.ylabel('Kullanım Sayısı')
plt.title('En Fazla Kullanılan 10 Mention')

plt.tight_layout()
plt.show()

# Belirli bir frekansın altındaki mention'ları filtreleme (örneğin, en az 5 kez kullanılan mention'ları göster)
min_frequency = 500
filtered_mentions = {mention: count for mention, count in mention_counter.items() if count >= min_frequency}

# Kelime bulutu oluşturma (mention'lar)
wordcloud = WordCloud(width=800, height=400, background_color='black').generate_from_frequencies(filtered_mentions)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud)
plt.title('Mention Word Cloud')
plt.axis('off')
plt.show()
