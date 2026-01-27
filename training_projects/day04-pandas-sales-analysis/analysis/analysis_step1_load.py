#amaç csv dosyasını güvenli şekilde oluşturmak ve veriyi tanımak 

import pandas as pd

# Dosya yolu
file_path = "data/daily_sales.csv"

# CSV dosyasını oku
df = pd.read_csv(file_path)

# İlk 5 satırı incele
print(df.head())

# DataFrame genel bilgisi
print(df.info())

# Sayısal kolonlar için özet istatistik
print(df.describe())

# Kolon isimleri
print(df.columns)
# Eksik değer kontrolü
print(df.isnull().sum())
