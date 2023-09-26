#! /usr/bin/python 3



# Script:   code challenge 3              
# Author: Raheem Sharif Reed                     
# Date of latest revision: July 17,2023     
# Purpose:In Python, create a script that utilizes the cryptography library to:
#Prompt the user to select a mode:
#Encrypt a file (mode 1)
Decrypt a file (mode 2)
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




from cryptography.fernet import Fernet

# Function to generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

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

# Function to encrypt a string
def encrypt_string(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    print("Ciphertext:", encrypted_text.decode())

# Function to decrypt a string
def decrypt_string(ciphertext, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(ciphertext.encode())
    print("Cleartext:", decrypted_text.decode())

# Main function
def main():
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n"))

    if mode == 1 or mode == 2:
        file_path = input("Enter the file path: ")
        key = load_key()

        if mode == 1:
            encrypt_file(file_path, key)
            print("File encrypted successfully.")
        else:
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
    elif mode == 3 or mode == 4:
        text = input("Enter the text: ")
        key = load_key()

        if mode == 3:
            encrypt_string(text, key)
        else:
            decrypt_string(text, key)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
