# =============================================================================
#  question4.py
#  The program prints the sum of squares of each line in a file.
#  Date: 02/09/2020
#  Author: Tarini Dash
# def main():
# =============================================================================
    print("The program prints the sum of squares of each line in a file.")
    # body of the program
    file_name = input("Enter the name of file with numbers : ")
    local_file= open(file_name, "r")
    master_list = local_file.read().splitlines()
    for i in range(len(master_list)):
        print("Sum of squares in line",i,"is", end=" ")
        to_numbers(master_list[i].split())
    local_file.close()


def square_each(nums):
    for i in range(0,len(nums)):
        nums[i] = nums[i]*nums[i]
    sum = sum_list(nums)
    print(sum)
        
        
def sum_list(nums):
    sum = 0
    for item in nums:
        sum = sum + item
    return sum

def to_numbers(str_list):
    for i in range(0,len(str_list)):
        str_list[i] = eval(str_list[i])
    square_each(str_list)

        
main()