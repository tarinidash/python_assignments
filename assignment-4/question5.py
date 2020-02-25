# question5.py
# The program counts number of words in an input file.
# Date: 02/05/2020
# Author: Tarini Dash
def main():
    print("The program counts number of words in an input file.")
    # body of the program
    file_name = input("Enter a file name: ")
    local_file= open(file_name, "r")
    words = local_file.read().split()
    print("There are",len(words),"words in the file.")
    
main()