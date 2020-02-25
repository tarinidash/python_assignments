# =============================================================================
#  question5.py
#  The program counts and returns the number of digits in a string line.
#  Date: 02/09/2020
#  Author: Tarini Dash
# =============================================================================
def main():
    print("The program counts and returns the number of digits in a string line")
    # body of the program
    file_name = input("Enter the name of file with numbers : ")
    local_file= open(file_name, "r")
    master_list = local_file.read().splitlines()
    for item in master_list:
        print("There are",count_digits(item),"in line",master_list.index(item)+1)
    local_file.close()

def count_digits(line):
    sum = 0
    for i in range(len(line)):
        if(line[i].isdigit()):
            sum = sum + 1
    return sum
          

main()