#! /usr/bin/python 3

#Reference: Chat Gpt Assisted

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

def search_files(directory, filename):
    num_files_searched = 0
    num_hits = 0

    for root, _, files in os.walk(directory):
        for file in files:
            num_files_searched += 1
            if filename in file:
                num_hits += 1
                print(f"Hit! File '{file}' found in '{os.path.join(root, file)}'")

    return num_files_searched, num_hits

def main():
    filename = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    if not os.path.exists(directory):
        print("Directory not found.")
        return

    num_files_searched, num_hits = search_files(directory, filename)

    print("\nSearch summary:")
    print(f"Files searched: {num_files_searched}")
    print(f"Hits found: {num_hits}")

if __name__ == "__main__":
    main()
