r'''
Task Description:
In this task, you are assigned to develop one program to help users calculate 
different information based a series of user provided numbers (integers). 
Detailed requirement is provided as follows: 

Input: A series of numbers 
Output: (Your output should be in one line)
	. The summation of the even numbers and summation of the odd numbers in 
       the input list 
	. The difference between the biggest and smallest numbers in the input list
	. The count of even numbers and odd numbers in the input list
	. The "centered" average of the list of integers. The centered average can be 
       calculated as the mean average of the values, after removing the largest and 
       smallest values in the array. If there are multiple copies of the smallest 
       value, ignore all but keep just one copy, and likewise for the largest value. 
       For instance, [12,2,8,7,100] -> 9; [2,2,8,11,100] -> 7

To have a better understanding of the loops, please try to implement 
two programs: one uses "for" and another uses "while" loop.

Running Examples:

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 12,2,8,7,100
The sum of all even numbers is 122, the sum of all odd numbers is 7, the difference between the biggest and smallest number is 98, the total number of even numbers is 4, the total number of odd numbers is 1, the centered average is 9.

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 1,2,abcd,8,11,200,301
Please enter valid integers.
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def EvenOddCalculator():
    all_numbers = []
    even = []
    odd = []
    try:
        all_numbers = [int(number) for number in sys.argv[1].split(",")]
    except:
        print("Please enter valid integers.")
        return
    all_numbers.sort()

    for number in all_numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    even_sum = sum(even)
    odd_sum = sum(odd)
    big_small_diff = all_numbers[-1]-all_numbers[0]
    total_even_num = len(even)
    total_odd_num = len(odd)
    centered_average = int(sum(all_numbers[1:-1])/len(all_numbers[1:-1]))

    print(f"The sum of all even numbers is {even_sum}, the sum of all odd numbers is {odd_sum}, the difference between the biggest and smallest number is {big_small_diff}, the total number of even numbers is {total_even_num}, the total number of odd numbers is {total_odd_num}, the centered average is {centered_average}.")


if __name__=='__main__':
    EvenOddCalculator()