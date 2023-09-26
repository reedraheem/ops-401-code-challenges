#! /usr/bin/python 3



# Script:   code challenge 15          
# Author: Raheem Sharif Reed                     
# Date of latest revision: August 21,2023      
# Purpose:prompt the user to type in a file name to search for
#prompt the user for a directory to search in
#search each file in the directory by name
#for each positive detection,print to the screen the file name and location
#at the end of the search process,print to the screen how many files were searched and how many hits were found.
#this script must successfully execute on both ubuntu linux 20.04 focal fossa and windows 10


import os
import platform

def search_files(directory, filename):
    hits = 0
    searched_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if filename in file:
                hits += 1
                print(f"Hit: {file} - Location: {os.path.join(root, file)}")
            searched_files += 1
    
    return searched_files, hits

def main():
    filename = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    if platform.system() == "Windows":
        directory = directory.replace("/", "\\")
    
    searched_files, hits = search_files(directory, filename)

    print(f"\nSearch Summary:")
    print(f"Total files searched: {searched_files}")
    print(f"Total hits found: {hits}")

if __name__ == "__main__":
    main()

