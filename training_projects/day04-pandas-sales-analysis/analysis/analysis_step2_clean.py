# bu veri temizleme adımıdır

import pandas as pd

# Veri setini yükle
file_path = "data/daily_sales.csv"
df = pd.read_csv(file_path)

# Eksik değer kontrolü
print("Missing values:")
print(df.isnull().sum())

# Veri tipleri kontrolü
print("\nData types:")
print(df.dtypes)

# Sales kolonunu garantiye al
df["sales"] = df["sales"].astype(int)

# Mantıksız (negatif) satış var mı?
print("\nNegative sales check:")
print(df[df["sales"] < 0])

# Temiz veri özet istatistik
print("\nClean data summary:")
print(df.describe())
# Temizlenmiş veriyi kaydet
clean_file_path = "data/daily_sales_clean.csv"
df.to_csv(clean_file_path, index=False)
print(f"\nCleaned data saved to {clean_file_path}")