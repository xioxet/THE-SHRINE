import sys


def BMICalculator():
    try:
        mode, height, weight = sys.argv[1:]
        assert mode in ['imperial', 'metric'] 
        
        bmi = float(weight) / (float(height) * float(height))
        
        bmi = int(bmi)
        if mode == 'imperial': bmi *= 703

        if (bmi <= 16):
                rating = 'Severe Thinness'
        if 16 < bmi <= 17:
                rating = 'Moderate Thinness'
        if 17 < bmi <= 18.5:
                rating = 'Mild Thinness'
        if 18.5 < bmi <= 25:
                rating = 'Normal'
        if 25 < bmi <= 30:
                rating = 'Overweight'
        if 30 < bmi <= 35:
                rating = 'Obese Class I'
        if 35 < bmi <= 40:
                rating = 'Obese Class II'
        if 40 < bmi:
                rating = 'Obese Class III'

        print(f"{bmi:0.2f}\t{rating}")

    except Exception as e:
        print('Your input is invalid!')

