import pandas as pd

df = pd.read_csv("data/ogrenciler.csv") # csv'deki verileri okumasını sağlayan satır. 

print("📂 CSV'DEN OKUNAN VERİ:")
print(df)

print("\n🎓 Bölüme göre not ortalaması:")
print(df.groupby("bolum")["not"].mean())
# groupby - > Veriyi gruplar, sonra her grup için hesaplama yapar.