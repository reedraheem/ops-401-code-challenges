#! /usr/bin/python 3



# Script:   code challenge 4              
# Author: Raheem Sharif Reed                     
# Date of latest revision: July 18,2023     
# Purpose:In Python, create a script that utilizes the cryptography library to:
#Prompt the user to select a mode:
#Encrypt a file (mode 1)
#Decrypt a file (mode 2)
#Encrypt a message (mode 3)
#Decrypt a message (mode 4)
#If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
#If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
#Depending on the selection, perform one of the below functions. You’ll need to create four functions:
#Encrypt the target file if in mode 1.
#Delete the existing target file and replace it entirely with the encrypted version.
#Decrypt the target file if in mode 2.
#Delete the encrypted target file and replace it entirely with the decrypted version.
#Encrypt the string if in mode 3.
#Print the ciphertext to the screen.
#Decrypt the string if in mode 4.
#Print the cleartext to the screen.
#Recursively encrypt a single folder and all its contents.
#Recursively decrypt a single folder that was encrypted by this tool.


import os
from cryptography.fernet import Fernet

# Function to generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Function to load the encryption key
def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Function to encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Function to encrypt all files in a folder and its subfolders
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Function to decrypt all files in a folder and its subfolders
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

# Main function
def main():
    if not os.path.exists("key.key"):
        generate_key()

    mode = int(input("Select a mode:\n1. Encrypt a folder\n2. Decrypt a folder\n"))

    folder_to_encrypt = input("Enter the folder path: ")

    key = load_key()

    if mode == 1:
        encrypt_folder(folder_to_encrypt, key)
        print("Folder encrypted successfully.")
    elif mode == 2:
        decrypt_folder(folder_to_encrypt, key)
        print("Folder decrypted successfully.")
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()

