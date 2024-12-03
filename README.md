# Analisis Performansi Ridge dan Lasso Regression

Repositori ini berisi analisis performansi model Ridge dan Lasso regression, dengan fokus pada evaluasi hasil pada data training, validasi, dan test. Notebook ini mengevaluasi model menggunakan metrik statistik utama dan memberikan wawasan tentang kemampuan generalisasi model. Model ini dirancang untuk memprediksi harga rumah di Boston berdasarkan berbagai variabel yang relevan.

---

## Ikhtisar Proyek
Ridge dan Lasso regression adalah teknik regularisasi regresi linier yang digunakan untuk mencegah overfitting dan meningkatkan performa model. Proyek ini membandingkan kedua metode menggunakan metrik performa berikut:

- **R-squared (R²)**: Mengukur proporsi varians yang dijelaskan oleh model.
- **Mean Absolute Error (MAE)**: Rata-rata dari selisih absolut antara nilai prediksi dan nilai aktual.
- **Root Mean Squared Error (RMSE)**: Akar kuadrat dari rata-rata selisih kuadrat antara nilai prediksi dan aktual.
- **Mean Absolute Percentage Error (MAPE)**: Rata-rata persentase kesalahan absolut antara nilai prediksi dan aktual.

Analisis ini menyoroti kekuatan dan kelemahan kedua model pada berbagai pembagian data.

---

## Penjelasan Variabel Dataset
Dataset ini berisi data yang digunakan untuk memprediksi harga rumah di Boston berdasarkan beberapa faktor. Berikut adalah penjelasan rinci masing-masing variabel:

1. **Criminal rate (crim)**:
   - Tingkat kriminalitas di daerah tersebut. Semakin tinggi nilai, semakin tinggi tingkat kriminalitas.

2. **Residential land zoned proportion (zn)**:
   - Proporsi luas tanah yang terzonasi untuk perumahan. Angka lebih tinggi menunjukkan lebih banyak area perumahan.

3. **Non-retail business acres proportion (indus)**:
   - Proporsi area untuk bisnis non-ritel, seperti industri atau pabrik.

4. **Is bounds with river (chas)**:
   - Variabel biner (0 atau 1) yang menunjukkan apakah area berbatasan dengan sungai.

5. **Nitrogen oxides concentration (nox)**:
   - Konsentrasi nitrogen oksida di udara, yang berhubungan dengan tingkat polusi.

6. **Number rooms average (rm)**:
   - Rata-rata jumlah kamar di setiap rumah di daerah tersebut.

7. **Owner age proportion (age)**:
   - Proporsi usia pemilik rumah di daerah tersebut. Angka tinggi menunjukkan komunitas dengan populasi yang lebih tua.

8. **Weighted distance to cities (dis)**:
   - Jarak ke pusat kota, dengan bobot tertentu berdasarkan lokasi geografis.

9. **Accessibility index (rad)**:
   - Indeks aksesibilitas ke fasilitas penting, seperti jalan raya atau transportasi umum.

10. **Tax rate (tax)**:
    - Tingkat pajak properti di area tersebut.

11. **Pupil-teacher ratio (ptratio)**:
    - Rasio jumlah siswa per guru di sekolah di area tersebut.

12. **Black proportion (black)**:
    - Proporsi penduduk dengan latar belakang ras tertentu.

13. **Percent lower status (lstat)**:
    - Persentase penduduk dengan status ekonomi lebih rendah.

14. **Median value of owner-occupied homes (medv)**:
    - Nilai tengah dari harga rumah yang dihuni oleh pemilik. Variabel ini adalah target prediksi.

---

## Hasil Utama
### Performansi Ridge Regression
#### Data Training
- **R-squared**: 73.95%
- **MAE**: 3.33
- **RMSE**: 23.25
- **MAPE**: 16.10%

#### Data Validasi
- **R-squared**: 71.06%
- **MAE**: 3.32
- **RMSE**: 20.35
- **MAPE**: 16.10%

#### Data Test
- **R-squared**: 70.30%
- **MAE**: 3.40
- **RMSE**: 25.93
- **MAPE**: 18.57%

### Performansi Lasso Regression
Hasil performa mirip dengan Ridge Regression namun nilai lasso lebih baik sedikit, variasi dalam metrik seperti R-squared (dijelaskan lebih rinci dalam notebook).

---

## Kesimpulan dan Asumsi
### Kesimpulan
- **Stabilitas**: Ridge Regression menunjukkan performa konsisten di antara data training, validasi, dan test.
- **Tidak Overfitting**: Tidak ada penurunan performa signifikan antara data training dan validasi/test.
- **Perbandingan**: Ridge dan Lasso Regression memiliki performa serupa dengan keunggulan kecil pada stabilitas Lasso Regression.

### Asumsi
1. **Data Bebas Multikolinearitas Berlebihan**: Ridge dan Lasso efektif dalam menangani multikolinearitas.
2. **Distribusi Data yang Wajar**: Asumsi bahwa data tidak memiliki outlier ekstrem yang memengaruhi performa model.
3. **Kesesuaian Model Linier**: Diasumsikan hubungan antara fitur dan target bersifat linier.

---

## Pengembangan Lebih Lanjut
- **Visualisasi Data**: Menambahkan visualisasi untuk menunjukkan hubungan antar fitur dan target.
- **Penerapan Hyperparameter Tuning**: Mengoptimalkan parameter seperti alpha untuk performa lebih baik.
- **Evaluasi Model Lain**: Membandingkan performa dengan model non-linear seperti Random Forest atau Gradient Boosting.
- **Penggunaan Data Nyata**: Menguji model dengan dataset baru untuk validasi tambahan.

---

## Cara Menggunakan
1. Clone repositori ini:
   ```bash
   https://github.com/NanasAlpukat/housing_price_prediction_api.git
   ```
2. Install dependensi (jika diperlukan) menggunakan:
   ```bash
   pip install -r requirements.txt
   ```
3. Buka notebook:
   ```bash
   jupyter notebook RedgeLassoReg.ipynb
   ```
4. Jalankan sel untuk mereproduksi analisis.

---

## Dependencies
- Python 3.12.7
- Libraries:
  - NumPy
  - Pandas
  - Scikit-learn
  - Matplotlib (opsional untuk visualisasi)

---

## Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat file LICENSE untuk detail.

---

## Penghargaan
Terima kasih kepada para kontributor dan komunitas open-source atas alat dan kerangka kerja mereka yang memungkinkan proyek ini.



---

# Flask API untuk Prediksi Harga Rumah

Repositori ini berisi aplikasi **Flask API** yang menyediakan dua endpoint utama:
1. **Auth Endpoint**: Untuk autentikasi pengguna dan menghasilkan JWT token (Access Token dan Refresh Token).
2. **Prediction Endpoint**: Untuk memprediksi harga rumah berdasarkan data yang diberikan, hanya dapat diakses dengan token valid.

## Struktur Proyek

```
flaskApi/
│
├── app.py                 # File utama untuk menjalankan aplikasi Flask
├── env                    # Tempat menyimpan file model machine learning
│   
├── routes/                # Folder untuk menyimpan file routes/controller
│   ├── __init__.py
│   ├── auth.py            # Auth route
│   ├── prediction.py      # Prediction route
├── models/                # Folder untuk model atau konfigurasi
│   └── jwt_utils.py       # Fungsi untuk JWT token (misalnya, generate, verify)
├── requirements.txt       # Daftar dependencies (Flask, PyJWT, etc.)
└── config.py              # Konfigurasi untuk Flask dan JWT Secret
```

## Cara Penggunaan

### 1. **Clone Repositori**
Untuk memulai, clone repositori ini ke mesin lokal Anda:

```bash
git https://github.com/NanasAlpukat/housing_price_prediction_api.git
```

### 2. **Instalasi Dependencies**

Setelah repositori ter-clone, masuk ke folder proyek dan install dependencies yang diperlukan:

```bash
pip install -r requirements.txt
```

### 3. **File Konfigurasi**

Pastikan Anda sudah mengatur file `.env` yang berisi konfigurasi seperti `SECRET_KEY` dan parameter terkait JWT. Misalnya:

```
SECRET_KEY=your-secret-key
JWT_ACCESS_TOKEN_EXPIRES=3600  # 1 hour
JWT_REFRESH_TOKEN_EXPIRES=86400  # 24 hours
```

### 4. **Jalankan Aplikasi**

Jalankan aplikasi Flask dengan menjalankan perintah berikut:

```bash
python app.py
```

Aplikasi akan berjalan pada `http://127.0.0.1:5000/` secara default.

### 5. **Endpoint API**

#### **Auth Endpoint (`/auth/code_unique`)**
Untuk melakukan login dan mendapatkan token:

- **Metode**: `POST`
- **Request Body**:
  ```json
  {
      "unique": "admin"
  }
  ```
- **Response**:
  - Jika berhasil, Anda akan menerima response dengan token yang diset dalam cookies:
    ```json
    {
        "message": "Login successful"
    }
    ```

#### **Prediction Endpoint (`/api/predict`)**
Untuk melakukan prediksi harga rumah menggunakan model yang sudah dilatih. Endpoint ini memerlukan **Bearer token** dalam cookies.

- **Metode**: `POST`
- **Request Body**:
  ```json
  {
      "features": [value1, value2, value3, ..., valueN]
  }
  ```
- **Response**:
  - Jika token valid, akan diberikan hasil prediksi:
    ```json
    {
        "prediction": predicted_value
    }
    ```
  - Jika token tidak valid atau expired:
    ```json
    {
        "message": "Invalid or expired token"
    }
    ```

## Model Machine Learning

Model yang digunakan untuk prediksi harga rumah adalah model **Lasso Regression** yang telah dilatih menggunakan data yang relevan (seperti data harga rumah Boston). Model ini memanfaatkan fitur-fitur berikut untuk melakukan prediksi:

- **Criminal rate (crim)**
- **Residential land zoned proportion (zn)**
- **Non-retail business acres proportion (indus)**
- **And other housing-related features...**

### Model yang Digunakan:
- **Lasso Regression** (untuk prediksi harga rumah)
- **Scaler** (untuk menormalkan data)

Model disimpan dalam folder `env/` dan diload saat aplikasi berjalan.

## Dependencies

Aplikasi ini menggunakan dependensi berikut:

- **Python 3.x**
- **Flask**: Framework untuk membangun aplikasi web
- **PyJWT**: Untuk pembuatan dan verifikasi token JWT
- **Flask-Cors**: Untuk mengizinkan permintaan dari domain berbeda
- **joblib**: Untuk memuat dan menyimpan model machine learning

Anda dapat menginstal dependensi dengan menjalankan:

```bash
pip install -r requirements.txt
```

## Pengembangan Lebih Lanjut

Untuk pengembangan lebih lanjut, beberapa fitur yang dapat dipertimbangkan:

- **Penambahan Visualisasi Data**: Untuk membantu memahami hubungan antara fitur dan harga rumah.
- **Hyperparameter Tuning**: Untuk meningkatkan performa model.
- **Evaluasi Model Lain**: Bandingkan Lasso Regression dengan model lain seperti Random Forest atau Gradient Boosting.

## Referensi

- [PyJWT Documentation](https://pyjwt.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Scikit-learn: Lasso Regression](https://scikit-learn.org/stable/modules/linear_model.html#lasso)

---

