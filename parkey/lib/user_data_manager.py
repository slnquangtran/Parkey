import json
import os
from pathlib import Path
from typing import Dict, Optional, Tuple

from lib.utils import decrypt_data, derive_key, encrypt_data


class UserDataManager:
    def __init__(self, data_folder: Path):
        self.data_folder = data_folder
        self.data_folder.mkdir(exist_ok=True)
        self.user_data_file = self.data_folder / "users.json"

    def _load_user_data(self) -> Dict:
        if not self.user_data_file.exists():
            return {}
        with open(self.user_data_file, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def _save_user_data(self, data: Dict) -> None:
        with open(self.user_data_file, "w") as f:
            json.dump(data, f, indent=4)

    def create_user(self, username: str, password: str) -> bool:
        users = self._load_user_data()
        if username in users:
            return False  # User already exists

        salt = os.urandom(16)
        key = derive_key(password, salt)  # This key is for the master password, not for data encryption

        users[username] = {
            "salt": salt.hex(),
            "key": key.decode()
        }
        self._save_user_data(users)
        return True

    def authenticate_user(self, username: str, password: str) -> Optional[bytes]:
        users = self._load_user_data()
        user_data = users.get(username)
        if not user_data:
            return None

        salt = bytes.fromhex(user_data["salt"])
        key = derive_key(password, salt)
        
        if key.decode() == user_data["key"]:
            return key
        return None

    def get_user_data_path(self, username: str) -> Path:
        return self.data_folder / f"{username}.json"

    def get_user_password_profiles(self, username: str, key: bytes) -> Dict:
        user_data_path = self.get_user_data_path(username)
        if not user_data_path.exists():
            return {}
        
        with open(user_data_path, "rb") as f:
            encrypted_data = f.read()

        if not encrypted_data:
            return {}
            
        decrypted_data = decrypt_data(encrypted_data, key)
        return json.loads(decrypted_data)

    def save_user_password_profiles(self, username: str, key: bytes, data: Dict) -> None:
        user_data_path = self.get_user_data_path(username)
        encrypted_data = encrypt_data(json.dumps(data), key)
        with open(user_data_path, "wb") as f:
            f.write(encrypted_data)
