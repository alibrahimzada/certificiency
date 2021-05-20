from hashlib import sha256

class ICryptoHelper:

    def sha256_encrypt(self, username: str, password: str):
        pass


class CryptoHelper(ICryptoHelper):

    def sha256_encrypt(self, username, password):
        user_name = username.lower()
        hash_str = user_name[::-1] + password
        hashed_word = sha256(hash_str.encode('ascii')).hexdigest()
        return hashed_word
