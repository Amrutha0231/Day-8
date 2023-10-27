from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("my_key.key", "wb") as key_data:
    key_data.write(key)


with open("data.txt", "r") as file:
    data = file.read()

print("The actual Data before Encryption:\n ", data)

byte_data = data.encode()

f= Fernet(key)

encrypt_data = f.encrypt(byte_data)

with open("data.txt", "wb") as file:
    file.write(encrypt_data)

print("\nThe Encrypted data is:\n ", encrypt_data)

from cryptography.fernet import Fernet

with open("my_key.key" ,"rb") as my_key:
    key = my_key.read()

with open("data.txt", "rb") as file:
    encryp_data = file.read()

print("The Encrypted Data is:\n", encryp_data)

f = Fernet(key)

decrypt_data = f.decrypt(encryp_data)

print("\nThe Actual Data is:\n", decrypt_data.decode())