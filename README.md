# 🧠 Proyek Awal: Menyelesaikan Permasalahan Human Resources

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-brightgreen)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Metabase](https://img.shields.io/badge/Dashboard-Metabase-orange)
![Status](https://img.shields.io/badge/Status-Selesai-success)

---

## 📌 Business Understanding

Perusahaan **Jaya Jaya Maju** yang bergerak di bidang edutech menghadapi tantangan besar dalam mempertahankan karyawan. Tingginya angka _attrition_ (keluarnya karyawan) memengaruhi stabilitas operasional dan meningkatkan biaya rekrutmen. Oleh karena itu, dibutuhkan pemahaman yang lebih baik mengenai penyebab _attrition_ serta pendekatan prediktif untuk mengantisipasinya.

### 🎯 Permasalahan Bisnis

1. Tingginya tingkat karyawan keluar dari perusahaan (_attrition_).
2. Belum ada sistem analisis atau prediksi untuk memantau potensi karyawan yang akan keluar.
3. Perlu analisis terhadap faktor-faktor yang memengaruhi _attrition_.

---

## 📦 Cakupan Proyek

- Eksplorasi dan analisis dataset _employee attrition_.
- Preprocessing data dan penyeimbangan kelas menggunakan SMOTE.
- Membangun model prediktif dengan algoritma **XGBoost**, yang memberikan hasil lebih baik dibandingkan Random Forest.
- Menyimpan model ke file `.pkl` dan membuat script prediksi (`prediction.py`).
- Menyimpan hasil prediksi ke PostgreSQL.
- Membuat dashboard analisis dan prediksi attrition menggunakan **Metabase**.

---

## 🧲 Persiapan & Setup

### 📂 Sumber Data

Dataset diambil dari Kaggle: [Employee Data Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

### ⚙️ Environment Setup

```bash
# Membuat virtual environment
python -m venv venv

# Aktivasi environment
# Windows
venv\Scripts\activate
# MacOS/Linux
source venv/bin/activate

# Install dependensi
pip install -r requirements.txt
```

---

## 🤖 Model Prediksi

Model yang digunakan: **XGBoost**  
Alasan pemilihan: Performa evaluasi lebih baik dari model sebelumnya (Random Forest)

- ✅ **Oversampling** dilakukan menggunakan SMOTE.
- ✅ Model disimpan dalam: `model/xgboost_model.pkl`
- ✅ Prediksi dilakukan melalui: `prediction.py`
- ✅ Hasil prediksi disimpan ke: `PostgreSQL` (database `hr_attrition`, tabel `attrition_predictions`)

### 📚 Cara Menjalankan Script Prediksi

```bash
python prediction.py
```
Script akan:
- Membaca `employee_data.csv`
- Melakukan preprocessing dan prediksi
- Menyimpan hasil prediksi ke PostgreSQL secara otomatis

---

## 📊 Business Dashboard (Metabase)

Dashboard interaktif dibangun menggunakan **Metabase** dan terhubung langsung ke database PostgreSQL.

### Fitur Visualisasi:

- Filter berdasarkan **Education**, **EducationField**, **TrainingTimesLastYear**, dan **Predicted Attrition**
- Statistik prediksi karyawan keluar
- Distribusi berdasarkan kategori demografis dan departemen
- Visualisasi berbentuk **batang**, kecuali untuk total prediksi yang ditampilkan dalam bentuk **angka total**

### 🔐 Akses Metabase (setup lokal)

Gunakan login berikut saat pertama kali setup:

- **Email**: `root@mail.com`
- **Password**: `root123`

---

## ✅ Hasil & Insight

- Attrition rate perusahaan > 10%, artinya cukup tinggi dan perlu ditangani serius.
- Model XGBoost memiliki akurasi, precision, recall, dan F1-score yang **lebih baik** dari model sebelumnya.
- Model dapat digunakan sebagai alat bantu tim HR dalam mendeteksi risiko karyawan keluar.

---

## 🌟 Conclusion

Berdasarkan hasil analisis dan visualisasi:

- **Penyebab utama tingginya attrition** adalah faktor-faktor seperti **OverTime**, **rendahnya JobSatisfaction**, dan **MonthlyIncome** yang tidak kompetitif.
- **Karakteristik umum karyawan yang keluar**:
  - Sering bekerja lembur (OverTime)
  - Tingkat kepuasan kerja rendah
  - Penghasilan bulanan di bawah rata-rata
  - Jarang mengikuti pelatihan
  
Dashboard ini memungkinkan tim HR untuk mengenali pola-pola tersebut dan mengambil langkah preventif lebih awal.

---

## 🎯 Rekomendasi

- Fokus pada fitur penting seperti: `OverTime`, `JobSatisfaction`, `MonthlyIncome`
- Gunakan model ini dalam sistem HRIS untuk deteksi dini risiko attrition
- Evaluasi dan retrain model secara berkala
- Monitoring rutin melalui dashboard Metabase

---

## 🗂️ Struktur Folder Proyek

```
submission/
│
├── dataset/
│   └── employee_data.csv
│
├── model/
│   └── xgboost_model.pkl
│
├── <username_dicoding>-dashboard/
├── <username_dicoding>-video/
│
├── metabase.db.mv.db
├── notebook.ipynb
├── prediction.py
├── requirements.txt
└── README.md
```

---

## 🙋 Kontributor

**Zidan Alfariza Putra Pratama**  
💼 SMK Negeri 1 Cipeundeuy - RPL  
📚 Fokus pada Data Analytics & Machine Learning  
📧 Email: [zidanalfariza@gmail.com](mailto:zidanalfariza@gmail.com)  
🔗 GitHub: [github.com/ZidanAlfarizaPutraPratama](https://github.com/zidanAlfarizaPutraPratama)

---

## 📝 Lisensi

Proyek ini dibuat untuk keperluan edukasi dalam program **Dicoding - Belajar Penerapan Data Science**.  
Lisensi penggunaan bebas untuk non-komersial.