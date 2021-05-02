from hashlib import sha256

class ICryptoHelper:
    def sha256Encrypt(self, user_id: str, password: str):
        pass

    def encrypt(self, plain_text: str):
        pass

    def decrypt(self, encrypted_text: str):
        pass


class CryptoHelper(ICryptoHelper):

    def sha256Encrypt(self, user_id, password):
        user_id = user_id.lower()
        hashString = user_id[::-1] + password
        hashedWord = sha256(hashString.encode('ascii')).hexdigest()
        return hashedWord

