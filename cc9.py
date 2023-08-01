#! /usr/bin/python 3

#Reference: Chat Gpt Assisted

# Script:   code challenge 9           
# Author: Raheem Sharif Reed                     
# Date of latest revision: july 31, 2023      
# Purpose:In Python, create a script that prompts the user to select one of the following modes:Mode 1: Offensive; Dictionary Iterator
#Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
#Add a delay between words.
#Print to the screen the value of the variable.
#Mode 2: Defensive; Password Recognized
#Accepts a user input string.
#Accepts a user input word list file path.
#Search the word list for the user input string.
#Print to the screen whether the string appeared in the word list

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

if __name__ == "__main__":
    print("Select one of the following modes:")
    print("1. Iterate through a word list file and print words.")
    print("2. Search for a word in a word list file.")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        file_path = input("Enter the path to the word list file: ")
        delay = float(input("Enter the delay between words (in seconds): "))
        iterate_and_print(file_path, delay)
    elif choice == 2:
        word = input("Enter the word to search: ")
        file_path = input("Enter the path to the word list file: ")
        search_word_in_list(word, file_path)
    else:
        print("Invalid choice. Please select 1 or 2.")
