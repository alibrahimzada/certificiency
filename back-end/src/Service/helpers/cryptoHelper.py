from hashlib import sha256

class ICryptoHelper:
    def sha256Encrypt(self, user_email: str, password: str):
        pass

    def encrypt(self, plain_text: str):
        pass

    def decrypt(self, encrypted_text: str):
        pass


class CryptoHelper(ICryptoHelper):

    def sha256Encrypt(self, user_email, password):
        user_email = user_email.lower()
        hashString = user_email[::-1] + password
        hashedWord = sha256(hashString.encode('ascii')).hexdigest()
        return hashedWord