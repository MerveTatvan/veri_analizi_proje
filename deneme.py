import pandas as pd

df = pd.read_csv("data/ogrenciler.csv") 
print("📂 CSV'DEN OKUNAN VERİ:")
print(df)

print(df[df["not"] > 85].groupby("bolum")["isim"].count())
#
#Bu kod tam olarak şunu yapıyor:

#df["not"] > 85
#→ Notu 85’ten büyük olanları filtreler

#.groupby("bolum")
#→ Bölümlere göre gruplar

#["isim"].count()
#→ Her bölümde kaç öğrenci olduğunu sayar