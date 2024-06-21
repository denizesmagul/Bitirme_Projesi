import pandas as pd
import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Verisetini yükle
df = pd.read_csv('tweets.csv', low_memory=False)
turkish_tweets = df[df['language'] == 'tr']
turkish_tweets.to_csv('tweets1.csv', index=False)

# Verisetini tekrar yükle
df = pd.read_csv('tweets1.csv', low_memory=False)

# Türkçe dil desteğini yükle
nltk.download('stopwords')
nltk.download('punkt')

# Türkçe stop words'leri yükle (özel tanımlı stop words listesi)
custom_stopwords = [
    'acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'birkaç', 'birşey', 'biz', 
    'bu', 'çok', 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi', 'hem', 
    'hep', 'hepsi', 'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mu', 'mı', 
    'mi', 'nasıl', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 
    'sanki', 'şey', 'siz', 'şu', 'tüm', 've', 'veya', 'ya', 'yani','için','bir'
]
stop_words = set(custom_stopwords)



# Metin içerisindeki URL'leri, hashtag'leri ve linkleri kaldırmak için fonksiyon
def remove_patterns(text):
    # URL'leri kaldır
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    
    # Hashtag'leri kaldır
    text = re.sub(r"#\S+", "", text)
    
    # Kullanıcı isimlerini kaldır
    text = re.sub(r"@[^\s]+", "", text)
    
    # Boşlukları ve özel karakterleri temizle
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Noktalama işaretlerini kaldır
    text = re.sub(r'[^\w\s]', '', text)
    
    # Sayıları kaldır
    text = re.sub(r"\d+", "", text)
    
    # Küçük harfe çevir
    text = text.lower()
    
    # Stop words'leri kaldır
    tokenizer = TweetTokenizer()
    words = tokenizer.tokenize(text)
    words = [word for word in words if word not in stop_words]
    
   
    
    return ' '.join(words)

# 'content' sütunundaki metinleri temizle ve köklerini bul
df['content'] = df['content'].apply(lambda x: remove_patterns(x))

# Boş olan 'content' sütunundaki satırları sil
df = df.dropna(subset=['content'])
df = df[df['content'].str.strip().astype(bool)]

# Benzersiz tweetleri tweets2.csv dosyasına kaydet
unique_tweets = df.groupby('content')['language'].first().reset_index()
unique_tweets.to_csv('tweets2.csv', index=False)
