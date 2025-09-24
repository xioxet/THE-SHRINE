import sys
import traceback

def EvenOddCalculator():
    try:
        nums = [*map(int, sys.argv[1].split(','))]
        cnts = [0, 0]
        sums = [0, 0]

        for i in nums:
            cnts[i%2] = cnts[i%2] + 1
            sums[i%2] = sums[i%2] + i

        z = [max(nums), min(nums)]
        minmax = z[0] - z[1]
        new = []
        
        for i in nums:
            if i in z:
                if nums.count(i) > 1 and i not in new:
                    new.append(i)
            else:
                new.append(i)
        
        wt = sum(new) // len(new)

        print(f'The sum of all even numbers is { sums[0] }, the sum of all odd numbers is {sums[1]}, the difference between the biggest and smallest number is {minmax}, the total number of even numbers is { cnts[0] }, the total number of odd numbers is {cnts[1]}, the centered average is {wt}.')
    except: 
        print("Please enter valid integers.")
        traceback.print_exc()


if __name__ == "__main__":
    EvenOddCalculator()
