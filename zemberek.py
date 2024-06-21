import pandas as pd
from zemberek.morphology.turkish_morphology import TurkishMorphology
from zemberek.tokenization import TurkishTokenizer
# BU KODLARI COLABDA CALISTIRDIM
tokenizer = TurkishTokenizer.DEFAULT
morphology = TurkishMorphology.create_with_defaults()

def find_roots(text):
    tokens = tokenizer.tokenize(text)
    roots = []
    for token in tokens:
        analysis = morphology.analyze(token.content)
        if analysis.analysis_results:
            root = analysis.analysis_results[0].item.root
            roots.append(root)
    return ' '.join(roots)

# CSV dosyasını uygun bir karakter kodlamasıyla okuyun
encoding_list = ['utf-8', 'latin1', 'iso-8859-9']
for encoding in encoding_list:
    try:
        tweets_df = pd.read_csv('tweets2.csv', encoding=encoding)
        break
    except UnicodeDecodeError as e:
        print(f"Encoding {encoding} didn't work: {e}")

# Her bir tweetin kelime köklerini bulun ve yeni bir sütuna ekleyin
tweets_df['root_content'] = tweets_df['content'].apply(find_roots)

# Sonuçları yeni bir CSV dosyasına kaydedin
tweets_df.to_csv('tweets3.csv', index=False, encoding='utf-8')