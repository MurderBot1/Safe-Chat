# Example of using the CryptoTools module to encrypt and decrypt text
print("------------------------------------------------------------")
import os

directory = os.getcwd()
entries = [os.path.join(directory, entry) for entry in os.listdir(directory)]
print(entries)

print("------------------------------------------------------------")
import CryptoTools as CT

Key = "Aasdfdsafasdfasdfadsf"
Enc = CT.EncryptText("Potatos are bad for you", Key)
Dec = CT.DecryptText(Enc, Key)

print(Key)
print(Enc)
print(Dec)

# Run the GUI APP
print("------------------------------------------------------------")
import GUI