import pandas as pd

# 1. Veri Okuma
df = pd.read_csv("data/products.csv")

print("İlk 5 satır:")
print(df.head())
print("\nVeri Bilgisi:")
print(df.info())

# 2. Temel İnceleme
print("\nVeri Boyutu:", df.shape)
print("Kolonlar:", df.columns)

# 3. Filtreleme
print("\nPuanı 4'ten büyük ürünler:")
print(df[df["rating"] > 4])

print("\nFiyatı 50-150 arası ürünler:")
print(df[(df["price"] >= 50) & (df["price"] <= 150)])

print("\nElektronik olmayan ürünler:")
print(df[df["category"] != "Elektronik"])

# 4. Eksik Veri Analizi
print("\nEksik veri yüzdesi (%):")
print(df.isnull().mean() * 100)

print("\nEksik verisi olan satırlar:")
print(df[df.isnull().any(axis=1)])

# 5. Eksik Rating Doldurma (Kategori Ortalaması)
df["rating"] = df.groupby("category")["rating"].transform(
    lambda x: x.fillna(x.mean())
)

print("\nEksik rating doldurulduktan sonra:")
print(df)

# 6. Basit İçgörü
ortalama_fiyat = df["price"].mean()

print("\nElektronik kategorisinde fiyatı ortalamanın üstünde olan ürünler:")
print(
    df.loc[
        (df["category"] == "Elektronik") &
        (df["price"] > ortalama_fiyat),
        ["product_name", "price", "rating"]
    ]
)
print("\nKategori bazlı özet tablo:")
summary = df.groupby("category").agg({
    "price": "mean",
    "rating": "mean"
})

print(summary)
