import sys
import os
import traceback

def AverageCalculator():
    assert len(sys.argv) == 4, "Your input is invalid!"
    try:
        a, b, c = map(lambda x: float(x), sys.argv[1:])
        average = (a+b+c) / 3
        print(f'Average:{average:.2f}')

    except:
        traceback.print_exc()
        print("Your input is invalid!")


if __name__ == "__main__":
    AverageCalculator()
