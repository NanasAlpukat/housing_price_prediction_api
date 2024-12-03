from flask import Flask
from routes.auth import auth_bp
from routes.prediction import prediction_bp

app = Flask(__name__)
app.config.from_object('config.Config')



# Register Blueprint untuk routing
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(prediction_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)



























# from flask import Flask, request, jsonify
# import joblib
# import numpy as np

# # Load model dan scaler
# lasso_model = joblib.load('./lasso_model.pkl')
# scaler = joblib.load('./scaler.pkl')

# # Inisialisasi Flask
# app = Flask(__name__)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Ambil data dari request
#         input_data = request.json
#         features = np.array(input_data['features']).reshape(1, -1)
        
#         # Normalisasi data
#         scaled_features = scaler.transform(features)
        
#         # Prediksi
#         prediction = lasso_model.predict(scaled_features)
        
#         # Return hasil prediksi
#         return jsonify({'prediction': prediction[0]})
#         # return jsonify({'prediction': 'test'})
#     except Exception as e:
#         return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)
