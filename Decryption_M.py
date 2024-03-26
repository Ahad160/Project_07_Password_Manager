from cryptography.fernet import Fernet

def Decryption(DEC_Key,DEC_File):
    # Read the encryption key from the key file
    with open(DEC_Key, "rb") as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)

    # Read the encrypted text from the file
    with open(DEC_File, "rb") as file:
        encrypted_text = file.read()

    # Decrypt and print the original text
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()

    return decrypted_text