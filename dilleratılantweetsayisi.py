import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import ScalarFormatter

# Veri setini yükle
df = pd.read_csv('tweets.csv')

# 'language' kolonundaki NaN değerleri boş bir string ile doldur
df['language'] = df['language'].fillna('')

# 'language' kolonundaki metinleri bir liste olarak al
documents = df['language'].tolist()

# CountVectorizer nesnesini oluştur
vectorizer = CountVectorizer()

# Metin belgelerini vektörlere dönüştür
X = vectorizer.fit_transform(documents)

# Frekansları DataFrame'e dönüştür
language_counts = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Dil frekanslarını topla
total_counts = language_counts.sum()

# Dil isimlerini sıralı bir şekilde ve frekansları al
sorted_languages = total_counts.sort_values(ascending=False)
languages = sorted_languages.index
counts = sorted_languages.values

# En fazla kullanılan iki dili belirleme
most_common_languages = sorted_languages.head(2)

# Toplam kaç farklı dilde tweet olduğunu hesaplama
total_languages = len(sorted_languages)

# Sonuçları konsola yazdırma
print(f"Veri setindeki tweetlerin en fazla {most_common_languages.index[0]}, ikinci en fazla ise {most_common_languages.index[1]} olduğu belirlenmiştir.")
print(f"Toplam {total_languages} farklı dilde tweet atılmıştır.")

# Grafik ayarlarını yap
plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")

# Çizgi grafiğini çiz
plt.plot(languages, counts, linestyle='-', linewidth=2, alpha=0.7, color='b')

# Logaritmik ölçek kullan
plt.yscale('log')

# ScalarFormatter kullanarak y ekseni etiketlerini normal sayılar olarak ayarla
plt.gca().yaxis.set_major_formatter(ScalarFormatter())

plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.title('Tweetlerin Dil Dağılımları', fontsize=14)
plt.xlabel('Diller', fontsize=12)
plt.ylabel('Tweet Sayısı (log ölçeği)', fontsize=12)

# Grafik göstermek
plt.show()
