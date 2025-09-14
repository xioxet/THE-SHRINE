
from fractions import Fraction

'''converts a number from its binary representation to its decimal representation'''
def bin_to_int(binstr: str) -> int:
    # due to python's zero indexing this is extremely inelegant
    i = 0
    for exponent, base in enumerate(binstr):
        i += int(base) * 2 ** (len(binstr) - exponent - 1)
    return i
    

'''converts a 32 bit string to its corresponding floating point number'''
def bin_to_floating_point(binstr: str) -> int:

    # this is actually rather tricky to do, because if we use python's builtin operators for, say, exponentiating fractions and decimals, we inherently <lose> precision because the underlying structure python uses _is_ floats! so it's a bit shag. instead, i opted to go for _fractional_ representations, which are hopefully more elucidatory here - my hope is that walking through it in this manner helps provide you with some intuition for this format, which is kind of baroque.


    signed_bit = int(binstr[0])
    exponent = binstr[1:9]
    mantissa = binstr[9:]

    print(f'{signed_bit = }')
    print(f'{exponent = }')
    print(f'{mantissa = }')

    # to derive the actual exponent used, we subtract by 127
    shifted_exp = bin_to_int(exponent) - 127

    print(f'actual exp: {exponent} - 127 = {shifted_exp}')
    mantissa_val = 1

    print('starting mantissa calculations')
    print('---')
    for exponent, char in enumerate(mantissa):
        value = int(char) * Fraction(1, 2**(exponent + 1))
        if int(char):
            print(f'{exponent+1} : {mantissa_val} + 1 / (2 ** {exponent+1}) = {mantissa_val + value}')
        else:
            print(f'{exponent+1} : no add...')
        mantissa_val += value

    print('---')
    magnitude = mantissa_val * (2**shifted_exp)
    print(f'final calculation: {magnitude} = {mantissa_val} * 2 ** {shifted_exp}')
    if signed_bit:
        magnitude *= -1

    print(f'converting that to decimal, we get {magnitude} = {float(magnitude)}') 

if __name__ == '__main__':
    binstr = input('input a 32-bit binary string > ')
    bin_to_floating_point(binstr)
    

