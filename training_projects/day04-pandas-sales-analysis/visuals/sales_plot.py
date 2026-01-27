#gerekli kütüphaneleri içe aktar
import pandas as pd
import matplotlib.pyplot as plt

# Veri setini yükle
file_path = "data/daily_sales.csv"
df = pd.read_csv(file_path)

# Veri tipini garantiye al
df["sales"] = df["sales"].astype(int)

# X ve Y eksenleri
days = df["day"]
sales = df["sales"]

# Grafik oluştur
plt.figure(figsize=(8, 5))
plt.plot(days, sales, marker="o")

# Ortalama satış çizgisi
average_sales = sales.mean()
plt.axhline(y=average_sales, linestyle="--")

# Başlık ve etiketler
plt.title("Daily Sales Analysis")
plt.xlabel("Day")
plt.ylabel("Sales Amount")

# Gösterim
plt.tight_layout()
plt.show()
# Grafiği kaydet
output_path = "visuals/daily_sales_plot.png"
plt.savefig(output_path)
print(f"Sales plot saved to {output_path}")