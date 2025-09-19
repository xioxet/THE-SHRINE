r'''
Task Description:
In this task, you will develop a program to compute all the leap years within a 
specified time period. The user will input a start year and an end year. 
Your task is to determine how many leap years are included in this period and 
print out those leap years. 

The rule for determining leap years is as follows:
	. A year is called a leap year, if the year is perfectly divisible by 4 - except 
     for years which are both divisible by 100 and not divisible by 400. The second 
     part of the rule effects century years. 
     For example; the century years 1600 and 2000 are leap years, 
     but the century years 1700, 1800, and 1900 are not. This means that three times 
     out of every 400 years there are 8 years between leap years.

More information about the leap years rule can be found online. 

Input: Two numbers (one is the start year, and another is the end year)
Output: The number of leap years and all the leap years (Your output should be in one line)
Note: In case of invalid input, print the message "Your input is invalid!".

Running Examples:

C:\INF1002\Lab2\LeapYearCalculator> python LeapYearCalculator.py 1989 2000
The number of Leap Years is 3, the Leap Years are 1992, 1996, 2000
'''

import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def LeapYearCalculator():
     error="Your input is invalid!"
     if len(sys.argv) != 3:
          print(error)
     else:
          try: 
               StartYear = int(sys.argv[1])
               EndYear = int(sys.argv[2])
               CurrentYear = StartYear
               LeapYears = []

               while not CurrentYear > EndYear:
                    if CurrentYear % 4 == 0 and str(CurrentYear)[2:4] != "00":
                         LeapYears.append(CurrentYear)
                    elif str(CurrentYear)[2:4] == "00" and CurrentYear % 400 == 0:
                         LeapYears.append(CurrentYear)
                    CurrentYear += 1
               print(f"The number of Leap Years is {len(LeapYears)}, the Leap Years are {str(LeapYears)[1:-1]}")
          except:
               print(error)

if __name__=='__main__':
     LeapYearCalculator()
