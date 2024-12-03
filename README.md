<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }
        header {
            background: #333;
            color: #fff;
            padding: 10px 0;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #444;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        code {
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        .highlight {
            background: #e7f5ff;
            padding: 10px;
            border-left: 4px solid #1e90ff;
            margin: 10px 0;
        }
    </style>
    <title>Ridge dan Lasso Regression</title>
</head>
<body>
<header>
    <h1>Analisis Performansi Ridge dan Lasso Regression</h1>
</header>
<div class="container">
    <h2>Ikhtisar Proyek</h2>
    <p>Repositori ini berisi analisis performansi model Ridge dan Lasso regression, dengan fokus pada evaluasi hasil pada data training, validasi, dan test. Notebook ini mengevaluasi model menggunakan metrik statistik utama dan memberikan wawasan tentang kemampuan generalisasi model. Model ini dirancang untuk memprediksi harga rumah di Boston berdasarkan berbagai variabel yang relevan.</p>

    <h2>Penjelasan Variabel Dataset</h2>
    <ul>
        <li><strong>Criminal rate (crim)</strong>: Tingkat kriminalitas di daerah tersebut. Semakin tinggi nilai, semakin tinggi tingkat kriminalitas.</li>
        <li><strong>Residential land zoned proportion (zn)</strong>: Proporsi luas tanah yang terzonasi untuk perumahan. Angka lebih tinggi menunjukkan lebih banyak area perumahan.</li>
        <li><strong>Non-retail business acres proportion (indus)</strong>: Proporsi area untuk bisnis non-ritel, seperti industri atau pabrik.</li>
        <li><strong>Is bounds with river (chas)</strong>: Variabel biner (0 atau 1) yang menunjukkan apakah area berbatasan dengan sungai.</li>
        <li><strong>Nitrogen oxides concentration (nox)</strong>: Konsentrasi nitrogen oksida di udara, yang berhubungan dengan tingkat polusi.</li>
        <li><strong>Number rooms average (rm)</strong>: Rata-rata jumlah kamar di setiap rumah di daerah tersebut.</li>
        <li><strong>Owner age proportion (age)</strong>: Proporsi usia pemilik rumah di daerah tersebut. Angka tinggi menunjukkan komunitas dengan populasi yang lebih tua.</li>
        <li><strong>Weighted distance to cities (dis)</strong>: Jarak ke pusat kota, dengan bobot tertentu berdasarkan lokasi geografis.</li>
        <li><strong>Accessibility index (rad)</strong>: Indeks aksesibilitas ke fasilitas penting, seperti jalan raya atau transportasi umum.</li>
        <li><strong>Tax rate (tax)</strong>: Tingkat pajak properti di area tersebut.</li>
        <li><strong>Pupil-teacher ratio (ptratio)</strong>: Rasio jumlah siswa per guru di sekolah di area tersebut.</li>
        <li><strong>Black proportion (black)</strong>: Proporsi penduduk dengan latar belakang ras tertentu.</li>
        <li><strong>Percent lower status (lstat)</strong>: Persentase penduduk dengan status ekonomi lebih rendah.</li>
        <li><strong>Median value of owner-occupied homes (medv)</strong>: Nilai tengah dari harga rumah yang dihuni oleh pemilik. Variabel ini adalah target prediksi.</li>
    </ul>

    <h2>Hasil Utama</h2>
    <h3>Performansi Ridge Regression</h3>
    <div class="highlight">
        <p><strong>Data Training:</strong></p>
        <ul>
            <li><strong>R-squared</strong>: 73.95%</li>
            <li><strong>MAE</strong>: 3.33</li>
            <li><strong>RMSE</strong>: 23.25</li>
            <li><strong>MAPE</strong>: 16.10%</li>
        </ul>
        <p><strong>Data Validasi:</strong></p>
        <ul>
            <li><strong>R-squared</strong>: 69.06%</li>
            <li><strong>MAE</strong>: 3.32</li>
            <li><strong>RMSE</strong>: 20.35</li>
            <li><strong>MAPE</strong>: 16.10%</li>
        </ul>
        <p><strong>Data Test:</strong></p>
        <ul>
            <li><strong>R-squared</strong>: 69.81%</li>
            <li><strong>MAE</strong>: 3.40</li>
            <li><strong>RMSE</strong>: 25.93</li>
            <li><strong>MAPE</strong>: 18.57%</li>
        </ul>
    </div>

    <h2>Kesimpulan dan Asumsi</h2>
    <h3>Kesimpulan</h3>
    <ul>
        <li><strong>Stabilitas</strong>: Ridge Regression menunjukkan performa konsisten di antara data training, validasi, dan test.</li>
        <li><strong>Tidak Overfitting</strong>: Tidak ada penurunan performa signifikan antara data training dan validasi/test.</li>
        <li><strong>Perbandingan</strong>: Ridge dan Lasso Regression memiliki performa serupa dengan keunggulan kecil pada stabilitas Ridge Regression.</li>
    </ul>

    <h3>Asumsi</h3>
    <ul>
        <li><strong>Data Bebas Multikolinearitas Berlebihan</strong>: Ridge dan Lasso efektif dalam menangani multikolinearitas.</li>
        <li><strong>Distribusi Data yang Wajar</strong>: Asumsi bahwa data tidak memiliki outlier ekstrem yang memengaruhi performa model.</li>
        <li><strong>Kesesuaian Model Linier</strong>: Diasumsikan hubungan antara fitur dan target bersifat linier.</li>
    </ul>

    <h2>Pengembangan Lebih Lanjut</h2>
    <ul>
        <li><strong>Visualisasi Data</strong>: Menambahkan visualisasi untuk menunjukkan hubungan antar fitur dan target.</li>
        <li><strong>Penerapan Hyperparameter Tuning</strong>: Mengoptimalkan parameter seperti alpha untuk performa lebih baik.</li>
        <li><strong>Evaluasi Model Lain</strong>: Membandingkan performa dengan model non-linear seperti Random Forest atau Gradient Boosting.</li>
        <li><strong>Penggunaan Data Nyata</strong>: Menguji model dengan dataset baru untuk validasi tambahan.</li>
    </ul>

    <h2>Cara Menggunakan</h2>
    <ol>
        <li>Clone repositori ini:
            <pre><code>git clone https://github.com/yourusername/ridge-lasso-analysis.git</code></pre>
        </li>
        <li>Install dependensi (jika diperlukan) menggunakan:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Buka notebook:
            <pre><code>jupyter notebook RedgeLassoReg.ipynb</code></pre>
        </li>
        <li>Jalankan sel untuk mereproduksi analisis.</li>
    </ol>

    <h2>Dependencies</h2>
    <ul>
        <li><strong>Python 3.12.7</strong></li>
        <li><strong>Libraries:</strong>
            <ul>
                <li>NumPy</li>
                <li>Pandas</li>
                <li>Scikit-learn</li>
                <li>Matplotlib</li>
                <li>Seaborn</li>
            </ul>
        </li>
        <li><strong>Dataset:</strong> Boston Housing Dataset (dapat diakses melalui <code>sklearn.datasets.load_boston()</code> atau dataset lain yang serupa).</li>
    </ul>

    <h2>Referensi</h2>
    <ul>
        <li><a href="https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression">Ridge Regression (scikit-learn)</a></li>
        <li><a href="https://scikit-learn.org/stable/modules/linear_model.html#lasso">Lasso Regression (scikit-learn)</a></li>
        <li><a href="https://www.kaggle.com/c/boston-housing">Boston Housing Dataset (Kaggle)</a></li>
        <li><a href="https://towardsdatascience.com/machine-learning-performance-metrics-you-should-know-f244d21a1b3f">Machine Learning Performance Metrics (Towards Data Science)</a></li>
    </ul>

    <footer>
        <p style="text-align:center; font-size: 0.9em; color: #777;">&copy; 2024 Analisis Ridge dan Lasso Regression. Semua hak cipta dilindungi.</p>
    </footer>
</div>
</body>
</html>




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