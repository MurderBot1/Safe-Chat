# Example of using the CryptoTools module to encrypt and decrypt text
import CryptoTools as CT

Key = "Aasdfdsafasdfasdfadsf"
Enc = CT.EncryptText("Potatos are bad for you", Key)
Dec = CT.DecryptText(Enc, Key)

print(Key)
print(Enc)
print(Dec)

# Run the GUI APP
import GUI