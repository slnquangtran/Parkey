import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key(password: str, salt: bytes) -> bytes:
    """Derives a key from a password and salt using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_data(data: str, key: bytes) -> bytes:
    """Encrypts data using the derived key."""
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(encrypted_data: bytes, key: bytes) -> str:
    """Decrypts data using the derived key."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()
