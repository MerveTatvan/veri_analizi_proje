#sayı hesapları , karşılaştırma , filtreleme işlemleri yapılır

import pandas as pd

# Veri setini yükle
file_path = "data/daily_sales.csv"
df = pd.read_csv(file_path)

# Veri tipini garantiye al
df["sales"] = df["sales"].astype(int)

# Toplam satış
total_sales = df["sales"].sum()
print(f"Total sales: {total_sales}")

# Ortalama satış
average_sales = df["sales"].mean()
print(f"Average daily sales: {average_sales:.2f}")

# En yüksek satış günü
max_sales = df["sales"].max()
best_day = df[df["sales"] == max_sales]["day"].values[0]
print(f"Best sales day: {best_day} with {max_sales}")

# En düşük satış günü
min_sales = df["sales"].min()
worst_day = df[df["sales"] == min_sales]["day"].values[0]
print(f"Worst sales day: {worst_day} with {min_sales}")

# Ortalama üstü satış günleri
above_average_days = df[df["sales"] > average_sales]
print("\nDays with above average sales:")
print(above_average_days[["day", "sales"]])