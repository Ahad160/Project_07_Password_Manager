from cryptography.fernet import Fernet

def Encryption(DEC_Key,DEC_File):
    # Generate a random encryption key
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    file=open(DEC_File,'r')
    read=file.read()

    # Input text
    txt = read
    file.close()

    # Encrypt the text
    encrypted_text = cipher_suite.encrypt(txt.encode())

    # Save the encrypted text to a file
    with open(DEC_File, "wb") as file:
        file.write(encrypted_text)

    # Save the key to a file (keep this key secret for decryption)
    with open(DEC_Key, "wb") as key_file:
        key_file.write(key)
