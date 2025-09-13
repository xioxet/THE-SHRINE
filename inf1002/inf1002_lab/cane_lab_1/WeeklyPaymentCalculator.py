import sys
import traceback

def WeeklyPaymentCalculator():
    try:
        assert len(sys.argv) == 4
        working_hrs, normal_rate, overtime_rate = map(lambda x: float(x), sys.argv[1:])
        assert working_hrs <= 168
        ot_hrs = working_hrs - 40
        normal_salary = min(40, working_hrs) * normal_rate
        extra_salary = max(ot_hrs, 0) * overtime_rate

        print(f'Normal Salary:{normal_salary:.2f}, Extra Salary:{extra_salary:.2f}, Total Salary:{normal_salary+extra_salary:.2f}')

    except:
        print("Your input is invalid!")
