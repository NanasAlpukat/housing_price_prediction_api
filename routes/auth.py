from flask import Blueprint, request, jsonify, make_response
from models.jwt_utils import generate_access_token, generate_refresh_token

auth_bp = Blueprint('auth', __name__)

# Simulasi data pengguna
# users = {'user1': 'password1'}

@auth_bp.route('/code_unique', methods=['POST'])
def code_unique():
    data = request.get_json()
    # username = data.get('username')
    # password = data.get('password')
    unique = data.get('unique')

    if unique == 'admin':
        # Generate encrypted access and refresh token
        access_token = generate_access_token(unique)
        refresh_token = generate_refresh_token(unique)
        
        # Create response and set encrypted tokens as cookies
        response = make_response(jsonify({
            'message': 'Login successful',
        }))
        response.set_cookie('access_token', access_token, httponly=True, secure=False, max_age=3600)
        response.set_cookie('refresh_token', refresh_token, httponly=True, secure=False, max_age=86400)
        return response
    
    return jsonify({'message': 'Invalid credentials'}), 401
