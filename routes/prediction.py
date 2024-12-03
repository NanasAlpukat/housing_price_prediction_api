from flask import Blueprint, request, jsonify
from models.jwt_utils import decode_token  # Pastikan fungsi decode_token sudah sesuai
import joblib
import numpy as np

# Load model dan scaler
lasso_model = joblib.load('env/lasso_model.pkl')  # Pastikan path model dan scaler benar
scaler = joblib.load('env/scaler.pkl')  # Pastikan path scaler benar

# Inisialisasi Blueprint untuk route prediksi
prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route('/predict', methods=['POST'])
def predict():
    # Ambil token dari cookies
    encrypted_token = request.cookies.get('access_token')
    
    # Jika token tidak ditemukan, return error 403
    if encrypted_token is None:
        return jsonify({'message': 'Missing token'}), 403

    # Decode token
    payload = decode_token(encrypted_token)
    if payload is None:
        return jsonify({'message': 'Invalid or expired token'}), 401

    # Ambil data input dari request
    input_data = request.json

    # Cek apakah data 'features' ada dalam input
    if 'features' not in input_data:
        return jsonify({'message': 'Features missing from input'}), 400

    # Konversi data fitur menjadi numpy array dan reshape sesuai format model
    try:
        features = np.array(input_data['features']).reshape(1, -1)
    except Exception as e:
        return jsonify({'message': f'Error processing features: {str(e)}'}), 400

    # Pastikan fitur memiliki elemen yang valid
    if features.size == 0:
        return jsonify({'message': 'Invalid input data'}), 400

    # Normalisasi data menggunakan scaler
    try:
        scaled_features = scaler.transform(features)
    except Exception as e:
        return jsonify({'message': f'Error scaling features: {str(e)}'}), 500

    # Lakukan prediksi dengan model
    try:
        prediction = lasso_model.predict(scaled_features)
    except Exception as e:
        return jsonify({'message': f'Error making prediction: {str(e)}'}), 500

    # Kembalikan hasil prediksi
    return jsonify({'prediction': prediction[0]})

