# Topic 1: Digital Age

## Computers through the ages

- 1964: ENIAC, $63m^2$, 30 tons
- 1950: EDVAC, $45m^2$, 7850kg
- 1959-1965: 2nd Gen Mainframe Computer (IBM 7094), Transistor
- 1965-1971: 3rd Gen Mini Computer, Integrated Circuit
- 1971- now: 4th Gen Micro Computers, Very Large Scaale Integration

## Define Computer

- A programable machine designed to automatically carry out a seequence of arithmatic or logical operations

## Types of Computers

- Supercomputer
- Personal Computer (laptop, tablet, smartphone)
- Embedded Computer (Smartwatch, TV control box)

## Timing

- Majority of  digital circuits aree sychronus
- means have clock signal (heart bit of system hehehaha)

## Binary logic

- Positive logic: High = 1, Low = 0
- Negative logic: High = 0, Low = 1
- computer has 4 limits, making 3 bands: V(L min), V(L max), V(H min), V(H max)
- any voltage between V(L max) and V(H min) is part of unacceptable value
- 3 bands are High Unacceptable and Low

## Info Size

- Bit
- Byte, 8 Bits
- Word, 2 Bytes, 8 Bits
- Kilo, 1024
- Mega, 1024x1024 = 1048576
- Giga, 1024x1024x1024 = 1073741824
- Tera, 1024x Giga

Note: When refering to info size, kilo is 1024. When refering to speeds e.g. sample rate, kilo is 1000

## Bit importance

- MSB = Most significant bit i.e. bit representing largest value
- LSB = Least significant bit i.e. the ones bit

0000 0000  
^---------^  
MSB----LSB

## Analogue to Digial Signal

Sampling vs quantization
- Sampling is by time(x-axis)
- Quantization is by value(y-axis)
- Sampling is cutting up the signal into discrete time blocks 
- quantization is cuttin up the signal amplitude into equal steps

Nyquist Rate
- Sampling frequency must be more than 2x max frequency of input.
- f(sample) > 2x f(input)
- f(sample) cannot be equals to 2x f(input).
- If unlucky and f(sample)=2xf(input), possible to only sample the 0 value of the wave

> Sampling rates
>> 1s = 1Hz  
>> 1ms = 0.0001s = 1KHz  
>> 1us = 0.0001ms = 0.0000001s = 1MHz  
>> 1ns = 0.0001us = 0.0000001ms = 0.0000000001s = 1Ghz

Quantiztion steps should also be reasonably small.  
Example, input voltage 0.3, but quantize voltage is 1 and -1 then will have error.  
even for 1, 0.33, -0.33, -1, value of 0.35 will be rounded wrongly

Quantization will determine how many bits each channel needs per sample.  
Usually 8, 10, 12, 16, 24



# Topic 2: Number systems

## Positional Number systems

Decimal binary hexadecimal are positional number systems
the position of each digit determines and represents a diffrent power of 10, 2 or 8
You maybe able to determin which number system is being used based on which digits are present.
e.g.
- 90FE is cnfm hex
- 9081 maybe decimal or hex
- 1011 maybe decimal, hex or binary  


you denote the system y using subscript $_2$ or $_{16}$  
hex sometimes denoted with a 0x or H` as prefix

apparently you can write binary decimal as well  
$1011.11 = 1*2^3 + 1*2^1 + 1*2^0 + 1*2^{-1} + 1*2^{-2}$

## Signing a number

Sign-magnitude representation
- just means num is signed. does not tell you HOW it's signed

n=bit sign-magnitude binary can rep values from -(2^n-1^-1) to +(2^n-1^-1)  
e.g. 8 bit binary therefore can store up to 7 bit of value  
i.e. 127 +ve and -ve
also results in a +ve 0 and -ve 0 representation

1's complement is the WEIRD way to sign and is not used in computers  
the compleement of a binary digit is the invers of all the digits.  
i.e 010 for 2 then 101 is -2  
still uses MSB to rep +ve and -ve numbers, 0 = +ve, 1 = -ve  
1's complement more easy to use in circuits as you just NOT gate each binary digit.  
to derive -ve number for 1's complement, find +ve value first, then invert all bits

2's complement is the default way to sign
- take the +ve value and invert bit like 1s complement
- add 1
- finish
changes value range to -2^n-1^ to +(2^n-1^-1)
removes -0 representation

## addition, sub traction and overflow

+ve + +ve = +ve (possible over flow)  
-ve + -ve = -ve (possible over flow)  
+ve + -ve = +ve or -ve (NO over flow)

Assume next 2 cases are 4 bit only system

$$1111_2 + 1111_2 = [1]1110_2$$

^ in this case you run out of bits.  
so you change carry flag to 1  
but since MSB is still negative, logic is correct so overflow flag is still 0
_____________

$$10001_2 + 1010_2 = [1]0011_2$$

^ in this case also run out of bits.  
so you change carry flag to 1.  
since MSB is 0 but both initial values MSB was 1, logic has failed as output is positive.  
Thus, overflow flag must be changed to 1
______________

$$[1]0011_2 - 0110_2 = 1101_2$$
^ borrow imiginary bit, 3-6 = -3 so logic ok, no overflow  


$$[1]0110_2 - 0011_2 = 0011_2$$
^ borrow imiginary bit, 6-3 = 3 so logic ok, no overflow

$$[1]1010_2 - 00011_2 = 0111_2$$
  ????????????????


if number is positive, can extend leading bits with 0
e.g. 0011 = 0000 0011
if number is negative, can extend leading bits with 1
e.g. 1001 = 1111 1001

## IEEE-754 Mantissa

$$(-1)^{sign} * 1.mantissa *2^{(exponent-127)}$$


$25.75$ to IEEE-754  
split decimal into whole num and fractional  
whole: 25, fractional: 0.75  
Find binary equivalent of fractional part $$ 0.75*2 = 1.5 \ \ \ -> (1)$$ $$ 0.5*2 = 1.0 \ \ \ -> (1)$$  
binary equivalent: $11001.11_2$  
move binary point to the **left** until you get $1.matissa$ $$11001.11 -> 1.100111$$  
Note: Moved to left (4) times, this will be the Exponent  

- Sign: is +ve so sign = 0  
- Mantissa = 1.[100111] from 1.100111  
- Exponent : 4 = exp-127 => 131 = 10000011  

NOTE: Exponent is unsigned.

_______

$.75$ to IEEE-754  
split decimal into whole num and fractional  
whole: 0, fractional: 0.75  
Find binary equivalent of fractional part $$ 0.75*2 = 1.5\ \ \ -> (1)$$ $$ 0.5*2 = 1.0\ \ \ \ -> (1) $$  
binary equivalent: $0.11_2$  
move binary point to the **right** until you get $1.mantissa$  
$0.11 -> 1.1$  
Note Moved to right (1) times, This will be the exponent 
- Sign: is +ve so sign = 0  
- Mantissa = 1.[1] from 1.1  
- Exponent : -1 = exp+127 => 126 = 10000011  

NOTE: Exponent is unsigned.  
Exponent is how many times you shift the binary point to the left, in this case moved right so is -1 and change exponent bias 127 to +

## Gray code

only one bit change at a time  
00 -> 01 -> 11 -> 10  
cannot go from 01 -> 10

## Serial vs Parallel

Serial: transfer one bit at a time  
is slow  
use case: longer range transmission (USB, TCP/IP, RS232, SATA)  

Parallel: transfer multiple bits at once  
is fast  
Subhect to synchronisation issues
use case: short range communication (ATAPI, internal buses)

## Parity

used to identify errors by adding 1 bit to the data  
Parity bit is attached to a group of bits to make the total number of 1s in a group always even (Even parity) or always odd (Odd parity).  

Parity type is agreed between users before sending data
if error detected, parity cannot recover the data.
Parity can be added as LSB or MSB, depend on user agreement

Even: 1011 011[1]
Odd : 1011 011[0]

Other error detection: Cyclic redundancy check (CRC), Hamming code


# Topic 3: Combinatorial Circuits

Generally: Ture = 1, False = 0  
Logic circuits types:
- Combinatorial  
- - Output depends only on current inputs
- Sequential
- - Output depends not only on current inputs but past sequence of inputs

Basic logic ops:
- AND
- OR
- NOT
 
## AND

$Z_{AND} = A . B = A ∧ B$

0 AND 0 = 0
0 AND 1 = 0
1 AND 0 = 0
1 AND 1 = 1

## NAND

NOT AND

$Z_{NAND} = \bar{A . B} =$
0 NAND 0 = 1
0 NAND 1 = 1
1 NAND 0 = 1
1 NAND 1 = 0

## OR

$Z_{OR} = A + B = A ∨ B$

0 OR 0 = 0
0 OR 1 = 1
1 OR 0 = 1
1 OR 1 = 1

## NOR

NOT OR

$Z_{NOR} = \bar{A + B} =$
0 NOR 0 = 1
0 NOR 1 = 0
1 NOR 0 = 0
1 NOR 1 = 0

![Base Gates](<../../inf1003/inf1003_notes/jacob-images/Base-Gates.png>)

## Boolean algebra Characteristics:

Commutativity (flip inputs does not change outcome): x.y = y.x, x+y = y+x
Associativity (grouping operations does not change outcome): (x.y).z = x.(y.z), (x+y)+z = x+(y+z)
Distributivity ()