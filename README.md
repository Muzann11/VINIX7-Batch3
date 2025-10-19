# 🚗 Dashboard Analisis Auto MPG
### Modul 7 - Business Intelligence (Track B/2)
**Oleh:** Muhammad Fauzan  
**Tools:** Python (Panel + HvPlot)  
**Dataset:** [Auto MPG - UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/9/auto+mpg)

---

## 🎯 Tujuan Tugas
Membangun **dashboard interaktif berbasis kode** menggunakan **Panel + HvPlot** untuk mengeksplorasi dataset *Auto MPG* dari UCI.  
Dashboard ini menjawab pertanyaan analisis utama terkait efisiensi bahan bakar mobil berdasarkan fitur teknis seperti jumlah silinder, berat, dan tahun produksi.

---

## ❓ Pertanyaan Analisis
1. Bagaimana distribusi nilai `mpg` pada seluruh mobil?  
2. Apakah ada perbedaan rata-rata `mpg` berdasarkan jumlah silinder?  
3. Bagaimana hubungan antara `weight` dan `mpg`?  
4. Bagaimana tren rata-rata `mpg` dari tahun ke tahun?

---

## 🧩 Komponen Interaktif
| Komponen | Deskripsi |
|-----------|------------|
| **Widget 1** | `IntRangeSlider` → memilih rentang tahun model (1970–1982) |
| **Widget 2** | `CheckBoxGroup` → memilih asal mobil (USA, Europe, Japan) |
| **Chart 1** | Histogram distribusi nilai MPG |
| **Chart 2** | Bar chart rata-rata MPG berdasarkan jumlah silinder |
| **Chart 3** | Scatter plot hubungan Weight vs MPG |
| **Chart 4** | Line + scatter plot tren rata-rata MPG per tahun |

---

## 📊 Narasi Insight
📍 1. Distribusi Nilai MPG
- Nilai mpg dominan di rentang 15–30, menandakan mayoritas mobil memiliki efisiensi bahan bakar sedang.
- Mobil dari Eropa dan Jepang cenderung memiliki nilai mpg lebih tinggi dibanding mobil dari USA.

📍 2. Rata-rata MPG Berdasarkan Jumlah Silinder
- Mobil dengan 4 silinder jauh lebih efisien (mpg rata-rata > 30).
- Mobil 8 silinder cenderung boros (mpg < 20).

📍 3. Hubungan Weight vs MPG
- Terlihat korelasi negatif kuat antara berat mobil dan efisiensi bahan bakar.
- Semakin berat mobil, semakin rendah nilai mpg.

📍 4. Tren Rata-rata MPG per Tahun
- Terdapat tren peningkatan nilai mpg dari tahun 1970 hingga 1982.
- Hal ini menunjukkan adanya peningkatan teknologi otomotif menuju efisiensi energi yang lebih baik.
