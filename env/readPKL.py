# import joblib

# # Ganti dengan path file .pkl yang ingin Anda baca
# model = joblib.load('./lasso_model.pkl')

# print(model)

import joblib

# Ganti dengan path file .pkl yang ingin Anda baca
model = joblib.load('./lasso_model.pkl')

# Contoh data fitur untuk prediksi
features = [0.00632, 18.0, 2.31, 0, 0.538, 6.575, 65.2, 4.0900, 1, 296, 15.3, 396.90, 4.98]

# Melakukan prediksi
prediction = model.predict([features])

print("Prediksi harga rumah:", prediction)
