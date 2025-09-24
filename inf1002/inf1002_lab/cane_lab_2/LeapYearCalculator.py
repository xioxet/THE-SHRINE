import sys
import traceback


def LeapYearCalculator():
    try:
        xrange = lambda x, y: range(x, y+1)
        assert len(sys.argv) == 3
        years = [str(i) for i in xrange(*map(int, sys.argv[1:]))
                if i % 4 == 0
                or (i % 100 != 0 and i % 400 == 0)]
        print(f"The number of Leap Years is {len(years)}, the Leap Years are {','.join(years)}")
    except:
        print("Your input is invalid!")



if __name__ == "__main__":
    LeapYearCalculator()
