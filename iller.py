from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from collections import Counter
import pandas as pd
import re

tweets = pd.read_csv('tweets.csv')
# 6 Şubat depreminde etkilenen iller


# Tweetler içerisindeki il isimlerini bulalım
city_counts = Counter()
for tweet in tweets['content']:
    # İl isimlerini içeren bir regex pattern'i tanımlayalım
    pattern = r'\b(Adana|Gaziantep|Malatya|Adıyaman|Kahramanmaraş|Diyarbakır|Hatay|Elazığ|Osmaniye|Kilis|Şanlıurfa)\b'
    cities = re.findall(pattern, tweet)
    for city in cities:
        city_counts[city] += 1

# Wordcloud oluşturalım
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='black', 
                min_font_size = 10).generate_from_frequencies(city_counts)

# Wordcloud'u gösterelim
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()
