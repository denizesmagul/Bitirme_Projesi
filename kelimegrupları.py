from nltk import ngrams
from collections import Counter
import pandas as pd

# CSV dosyasını yükleyin
tweets = pd.read_csv('tweets3.csv')

# NaN değerleri boş string ile değiştirin
tweets['root_content'] = tweets['root_content'].fillna('')

# Tüm tweet içeriklerini bir metin olarak birleştirelim
text = ' '.join(tweets['root_content'])

# Metni token'lara ayıralım
tokens = text.split()

# 1-gram'ları oluşturalım
n = 1
ngrams_list1 = ngrams(tokens, n)

# 1-gram'ların frekansını hesaplayalım
ngrams_freq1 = Counter(ngrams_list1)

# En sık kullanılan 1-gram'ları bulalım
most_common_ngrams1 = ngrams_freq1.most_common(10)

# Sonuçları yazdıralım
print("En sık kullanılan 1-gram'lar:")
for ngram, freq in most_common_ngrams1:
    print(' '.join(ngram), ':', freq)

# 2-gram'ları oluşturalım
n = 2
ngrams_list2 = ngrams(tokens, n)

# 2-gram'ların frekansını hesaplayalım
ngrams_freq2 = Counter(ngrams_list2)

# En sık kullanılan 2-gram'ları bulalım
most_common_ngrams2 = ngrams_freq2.most_common(10)

# Sonuçları yazdıralım
print("En sık kullanılan 2-gram'lar:")
for ngram, freq in most_common_ngrams2:
    print(' '.join(ngram), ':', freq)


