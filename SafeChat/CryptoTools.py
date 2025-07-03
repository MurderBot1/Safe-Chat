import hashlib as HL
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def EncryptText(Data : str, Key : str):
    Key = HL.sha512(Key.encode()).digest()[:32]
    Padder = padding.PKCS7(128).padder()
    Data = Padder.update(Data.encode()) + Padder.finalize()
    Iv = os.urandom(16)
    F_Cipher = Cipher(algorithms.AES(Key), modes.CBC(Iv), backend=default_backend())
    Encryptor = F_Cipher.encryptor()
    CipherText = Encryptor.update(Data) + Encryptor.finalize()
    return base64.b64encode(Iv + CipherText).decode()

def DecryptText(EncodedData: str, Key: str) -> str:
    Key = HL.sha512(Key.encode()).digest()[:32]
    RawData = base64.b64decode(EncodedData)
    Iv = RawData[:16]
    CipherText = RawData[16:]
    F_Cipher = Cipher(algorithms.AES(Key), modes.CBC(Iv), backend=default_backend())
    Decryptor = F_Cipher.decryptor()
    DecryptedData = Decryptor.update(CipherText) + Decryptor.finalize()
    try:
        Unpadder = padding.PKCS7(128).unpadder()
        PlainText = Unpadder.update(DecryptedData) + Unpadder.finalize()
        return PlainText.decode(errors="replace")
    except ValueError:
        return DecryptedData.decode(errors="replace")
    return PlainText.decode()
