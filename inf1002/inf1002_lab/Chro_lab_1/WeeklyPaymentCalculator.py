r'''
Task Description:
Develop one employee weekly payment calculation program. 
The program requirement is as follows: 
1.	Allow users to run your program with three input arguments by passing three
    values to the program:  the number of working hours, input normal rate and 
    input the overtime rate.

2.	Your program will read the three arguments and calculate the users salary 
    using the following two formulas:
        a.	Payment of the normal hours = normal rate * normal hours
        b.	Payment of the overtime hours = overtime rate * overtime hours
        NOTE: the working hours within 40 belong to normal hours and those beyond 
              40 hours are considered as overtime hours. 

3.	After user inputs all the numbers, if the input numbers are invalid, you need 
    to present an error message "Your input is invalid!". Otherwise, you need to 
    print out the employee's payment of normal hours, his payment of overtime 
    hours and total payment. The output payment requires to have 2 precisions. 
    For instance, if payment is 2300.456, it should print 2300.46. 
    If payment is 2300, it should print 2300.00.
      
NOTE: You have to strictly follow the input and output format. 

Running example:
Assume your program is named as WeeklyPaymentCalculator.py. Example output is as follows: 

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 20 30 100
Normal Salary:600.00, Extra Salary:0.00, Total Salary:600.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 60 30 200
Normal Salary:1200.00, Extra Salary:4000.00, Total Salary:5200.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 10000 10 200
Your input is invalid!

'''
import sys
# You can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def WeeklyPaymentCalculator():
    error = "Your input is invalid!"
    if len(sys.argv) != 4:
        print(error)
    else:
        try:
            if float(sys.argv[1]) > 168:
                print (error)

            elif float(sys.argv[1]) <= 40:
                normal = float(sys.argv[1]) * float(sys.argv[2])
                print(f"Normal Salary:{normal:.2f}, Extra Salary:0.00, Total Salary:{normal:.2f}")
            else:
                normal = float(sys.argv[2]) * 40
                extra = (float(sys.argv[1]) - 40) * float(sys.argv[3])
                print(f"Normal Salary:{normal:.2f}, Extra Salary:{extra:.2f}, Total Salary:{normal + extra :.2f}")

        except ValueError:
            print(error)

if __name__=='__main__':
    WeeklyPaymentCalculator()