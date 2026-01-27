
-- Day06: SQL Basics
-- Konu: SELECT, WHERE, ORDER BY
-- Veri mantığı: daily_sales tablosu (day, sales)

-- 1️⃣ Tüm veriyi getir
SELECT * 
FROM daily_sales;

-- 2️⃣ Sadece sales kolonunu getir
SELECT sales
FROM daily_sales;

-- 3️⃣ 150'den büyük satışları getir
SELECT *
FROM daily_sales
WHERE sales > 150;

-- 4️⃣ Satışları büyükten küçüğe sırala
SELECT *
FROM daily_sales
ORDER BY sales DESC;




-- =========================
-- Day06 Step 2: GROUP BY
-- =========================

-- 5️⃣ Toplam kaç gün var?
SELECT COUNT(*) AS total_days
FROM daily_sales;

-- 6️⃣ Ortalama satış
SELECT AVG(sales) AS average_sales
FROM daily_sales;

-- 7️⃣ En yüksek ve en düşük satış
SELECT 
    MAX(sales) AS max_sales,
    MIN(sales) AS min_sales
FROM daily_sales;

-- 8️⃣ Günlere göre satış özeti (mantık egzersizi)
SELECT 
    day,
    sales
FROM daily_sales
ORDER BY sales DESC;




-- =========================
-- Day06 Step 3: CASE WHEN + GROUP BY
-- =========================

-- 9️⃣ Ortalama satışın üstünde mi?
SELECT
    day,
    sales,
    CASE
        WHEN sales > (SELECT AVG(sales) FROM daily_sales)
        THEN 'Above Average'
        ELSE 'Below Average'
    END AS sales_category
FROM daily_sales;

-- Day06 Step 3
-- Konu: GROUP BY, COUNT, AVG, MAX, MIN
-- Amaç: Pandas groupby mantığını SQL’de görmek

-- 1️⃣ Toplam gün sayısı
SELECT COUNT(*) AS total_days
FROM daily_sales;

-- 2️⃣ Ortalama satış
SELECT AVG(sales) AS average_sales
FROM daily_sales;

-- 3️⃣ En yüksek ve en düşük satış
SELECT 
    MAX(sales) AS max_sales,
    MIN(sales) AS min_sales
FROM daily_sales;

-- 4️⃣ Satış durumu etiketi (CASE WHEN)
SELECT
    day,
    sales,
    CASE
        WHEN sales > 150 THEN 'High'
        ELSE 'Normal'
    END AS sales_level
FROM daily_sales;

-- 5️⃣ Satış seviyesine göre özet
SELECT
    CASE
        WHEN sales > 150 THEN 'High'
        ELSE 'Normal'
    END AS sales_level,
    COUNT(*) AS day_count,
    AVG(sales) AS avg_sales
FROM daily_sales
GROUP BY sales_level;



