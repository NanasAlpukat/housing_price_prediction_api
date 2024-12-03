import jwt
import datetime
import base64
from cryptography.fernet import Fernet
from config import Config

# Generate a key for Fernet encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def generate_access_token(identity):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=Config.JWT_ACCESS_TOKEN_EXPIRES)
    token = jwt.encode({'identity': identity, 'exp': expiration}, Config.SECRET_KEY, algorithm='HS256')
    
    # Enkripsi token JWT
    encrypted_token = cipher_suite.encrypt(token.encode())
    
    # Encode hasil enkripsi ke Base64 agar bisa disimpan di cookie
    base64_encrypted_token = base64.urlsafe_b64encode(encrypted_token).decode()
    
    return base64_encrypted_token

def generate_refresh_token(identity):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=Config.JWT_REFRESH_TOKEN_EXPIRES)
    token = jwt.encode({'identity': identity, 'exp': expiration}, Config.SECRET_KEY, algorithm='HS256')
    
    # Enkripsi token JWT
    encrypted_token = cipher_suite.encrypt(token.encode())
    
    # Encode hasil enkripsi ke Base64 agar bisa disimpan di cookie
    base64_encrypted_token = base64.urlsafe_b64encode(encrypted_token).decode()
    
    return base64_encrypted_token

def decode_token(base64_encrypted_token):
    try:
        # Decode Base64 ke dalam bentuk byte
        encrypted_token = base64.urlsafe_b64decode(base64_encrypted_token.encode())  # Perbaiki: tambahkan .encode()
        
        # Dekripsi token
        decrypted_token = cipher_suite.decrypt(encrypted_token).decode()
        
        # Decode JWT
        payload = jwt.decode(decrypted_token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

