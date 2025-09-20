# Topic 1 Sequences

Sequences are ordered and may be infinite
- $(a_1,a_2,a_3,...)$

$a_n$ is a number  
$_n$ is the index

## Other Notation
- $∞$: infinity  
- $∈$: “is an element of”  
- $ℕ$ = 0, 1, 2, 3, ... : the set of natural numbers*  
- $ℤ$ = ... , −2, −1, 0, 1, 2, ... : the set of integers  
- $ℤ^+$ = 1, 2, 3, ... : the set of positive integers  
- $ℤ^−$ = ... , −3, −2, −1 : the set of negative integers  

if notation has subscript, 

## Important Formula

Number of terms  
for $\displaystyle\sum_{k=1}^5$, there are 5 terms,  
for $\displaystyle\sum_{k=0}^4$, there are also 5 terms  


to find num of terms for$\displaystyle\sum_{k=n}^p$: $$n-p+1$$
 


Arithmetic Series Summation  
General formula:
$$a_n = a+(n-1)d$$
Summation formula:
$$S_n = \frac{n[2a+(n-1)d]}{2}$$
$$= \frac{n(a_1+a_n)}{2}$$

Geometric Series Summation  
General Formula: 
$$a_n = ar^{n-1}$$
Summation Formula:  $$S_n = \frac{a(1 - r^n)}{1 - r} $$
$$ = \frac{a(r^n)-1}{r-1} $$

Infinite Summation 
$$S_∞=\frac{a}{1-r},\ \ \ \ when |r|<1,$$
$a$ is the first element in the sequence,  
$r$ is the ratio

## Recurrance relation

find out next element based on previous element

$$a_n = a_{n-1} [operand] [something]$$

Explicit (General) Formula: reflecting the correlation between term value and its index
$$a_n = f(n)$$

Reursive formula: reflecting the correlation between term value and the value(s) of prior term(s)
$$a_n =f(a_{n-1}),\ \ \  assuming\ (n>1)\ and\ a_1\ is\ given$$
Recurrance relations can use any operand.  
Only important part is that to find $a_{n+1}$, must use $a_n$ and cannot use $_n$

## Series Formula

able find any element based on index  
got 2 kinds, arithmetic and geometric

## Arithmatic Progression

is a sequence of numbers where the **difference** between 2 consective terms is the same

is a sequence with first term a and common difference d
has its terms given by a formula
e.g.  
$$a_n = a+(n-1)d$$

e.g. sequence is 5, 8, 11, 14

## Geometric Progression

is a sequence of numbers where the **ratio** between consecutive terms is the same

is a sequence with first term and common ratio 
has its terms given by a formula  
$$a_n = ar^{n-1}$$

## Summation
$\displaystyle\sum_{k=m}^n a_k = a_m + a_{m+1} + ... + a_n$  

when m=1, often use:  
$S_n = \displaystyle\sum_{k=1}^n a_k$

additivity:  
$\displaystyle\sum_{k=m}^n a_k + \displaystyle\sum_{k=m}^n b_k = \displaystyle\sum_{k=m}^n (a_k+b_k)$  
 
homogenity:  
$\displaystyle\sum_{k=m}^n ca_k = c\displaystyle\sum_{k=m}^n a_k$


**Arithmetic Series Summation**
$$S_n = \frac{n[2a+(n-1)d]}{2}$$
$$= \frac{n(a_1+a_n)}{2}$$

**Arithmetic Summation Application:**

Sum of all positive int $1\leq i \leq 100$  
$S_n = a_1 + ... + a_{100}$  
$= \frac{n[a_1+a_{100}]}{2}$  
$= \frac{100[1+100]}{2}$  
$= 5050$

**Geometric Series Summation**  
when n < ∞ :$$S_n = \frac{a(r^n-1)}{r-1} $$

when n approach ∞:
$$lim_{n->∞},\ \ \ S_n = \frac{a}{r-1}$$

**Geometric series summation application:**  

Investor adds $P$ dollars to an account at the beginning of each year.  
Interest rate $k$ paid at the end of the year  
At beginning of 2nd year, account will have $P(1+k)+P$
At yeat $t$, account will have $P + P(1+k) + ... +P(1+k)^{t-1}$  
  
Value when $t=50, P=100,k=0.01$:
$$S_t = \frac{P[(1+k)^t-1]}{(1+k)-1}$$
$$= \frac{P[(1+k)^t-1]}{k}$$
$$= \frac{100[(1+0.01)^50-1]}{0.01}$$
$$= \$6,446.32$$

## Series , Infinite Summation

Infinite Summation 
$$S_∞=\frac{a}{1-r},\ \ when \ |r|<1,$$
$a$ is the first element in the sequence,  
$r$ is the ratio

**Infinite Summation Application**

$S_∞ = \displaystyle\sum_{n=1}^∞ \frac{1}{3^n}$  
Since exponent in denominator, take out and put in brackets  
$S_∞ = \displaystyle\sum_{n=1}^∞ (\frac{1}{3})^n$  
This makes $\frac{1}{3}$ the ratio.  
So, using Geometric Series summation formula:  
$S_∞ = \frac{\frac{1}{3^1}}{1-\frac{1}{3}} = \frac{\frac{1}{3}}{\frac{2}{3}} = \frac{1}{3}*\frac{3}{2} = \frac{1}{2}$


# Topic 2 Number Theory

Purpose: Cryptography  
based on: factoring int into prime factor is hard  
$n = p*q$ where $p$ and $q$ are distinct primes

RSA = Rivest, Shamir adleman  
key length = 1024 - 4096 bits  
- in 2003 estimated 1024 RSA crackable by 2010  
- no evidence yet but minimum recommendation to use at least 2048 RSA

greatest common demoninator (gcd)

1. choose $p$ and $q$, find $n = p*q$
2. choose $e$ such that $gcd(e,(p-1)(q-1)) = 1$
3. solve $d*e == 1(mod(p-1)(q-1))$
4. pub key: ( e, n ), priv key: ( p, q, d )

in number theory,  
mod is modulo which is % in python  
not modulus where is absolute value |x|

## Key formulae

$$a = d*q +r$$
$$r = a \mod d$$

if $a ≡ b \mod m$ and $c ≡ d \mod m$:  

$$a + c ≡ b + d \mod m$$

$$a*c = b*d \mod m$$

given int $I$ and trying see if prime:  
largest number to check shld be $\sqrt{I}$

$$LCM = \frac{a * b}{GCD}\ \ \ \ OR\ \ \ \ GCD = \frac{a * b}{LCM}$$

## Division

a != 0  
a divides b means b/a no remainder  
a does not divide b means b/a have remainder

$$a = d*q+r$$
 a is dividen, d is divisor, q is quotient, r is remainder

## Division Algorithm

let $a$ be integer, $d$ be +ve integer.  
let $q$ and $r$ be unique with $0 <= r < d$

formula is thus

$$a = d*q +r$$
$$r = a \mod d$$


## Modular Arithmetic

≡ triple bar means congruent

$a ≡ b \mod{m}$  
is same as  
$a \mod{m} = b \mod{m}$

**Theorem**  
- let $m$ be +ve int  
- if $a ≡ b \mod{m}$ and $c ≡ d \mod{m}$
- then  
- $$a + c ≡ b + d (\mod{m})$$
- and  
- $$a*c = b*d (\mod{m})$$

Other equations:
- $(a+b)\mod{m} = ((a\mod{m})+(b\mod{m}))\mod{m}$
- $(a-b)\mod{m} = ((a\mod{m})-(b\mod{m}))\mod{m}$
- $(a*b)\mod{m} = ((a\mod{m})*(b\mod{m}))\mod{m}$
- $a^b\mod{m} = (a\mod{m})^b\mod{m}$

$98 \mod{97} = 1$  
$9800 \mod{97} ≡ 100 \mod{97} = 3$  
$98^5 \mod{97} ≡ 98 \mod {97} = 1$  
$10001 \mod{97} ≡ 301 \mod{97} ≡ 10$

## Primes

**Define prime**  
$p > 1$ and only positive factor is 1 and p  
if int $> 1$ and not prime, is a composite

**Theorem**  
every int $> 1$ can be written uniquely as a prime or as a product of 2 or more primes, where prime factors are written in order of non-decreasing size

**Theorem**  
if $n$ is composite int,  
then n has prime divisor $\leq \sqrt{n}$

^ can use theorem to check is num is prime, using brute force method called trial division
divide n by all primes no exceeding $\sqrt n$  
can conclude n is prime if n no divisible by any of these primes

**Theorem**  
there are infintely many primes

## Greatest common Divisor

GCD is the largest integer that divides 2 integers

let $a,b$ be int, non-zero  
largest int $d$ such that $d$ divides $a$ and $d$ divides $b$  
$d$ is therefore the GCD, denoted as $gcd(a.b)$

if $gcd(a, b) =1$  
$a$, $b$ are relatively prime  
e.g. 17 and 22 relatively prime but 22 is not actual prime

integers in set $a^1,a^2,...,a^n$ are pairwise relativly prime if  
$gcd (a^i, a^j) = 1$  when   $1 <= i < j <= n$  
e.g. determine if 10, 17 and 21 are pairwise relativly prime  
$gcd(10,17) =1$  
$gcd(10,21) =1$  
$gcd(17,21) =1$  
thus they are pairwise relatively prime

suppose prime factorisation for +ve int a and b

$a = p_1^{a1},p_2^{a2}, ... ,p_n^{an}$  
$b = p_1^{b1},p_2^{b2}, ... ,p_n^{bn}$  

then, gcd(a,b) is given by  
$gcd(a,b) = p_1^{min(a1,b1)},p_2^{min(a2,b2)}, ... ,p_n^{min(an,bn)}$  
where $min(x,y)$ chooses the smaller of $x$ and $y$

## Least Common Multiple

Least Common Multiple LCM of positive int $a$ and $b$ is smallest possible int that is divisible by both $a$ and $b$  
denoted as $lcm(a.b)$

suppose prime factorisation for +ve int a and b

$a = p_1^{a1},p_2^{a2}, ... ,p_n^{an}$  
$b = p_1^{b1},p_2^{b2}, ... ,p_n^{bn}$  

then, lcm(a,b) is given by  
$gcd(a,b) = p_1^{max(a1,b1)},p_2^{max(a2,b2)}, ... ,p_n^{max(an,bn)}$  

where $max(x,y)$ chooses the larger of $x$ and $y$

$a,b$
$gcd(a,b) * lcm(a,b) = ab$

## Euclidian Algorithm

### Lemma

Let $a = dq+r$  
where $a$, $d$, $q$ and $r$ are int,  

Then, $$gcd(a,d) = gcd(d,r)$$  

lemma above gives us a more efficient method of finding the greatest common divisor,
called the Euclidean algorithm.  

To find gcd(287,91), divide 287 by 91

$$287 = 91 * 3 +14$$

Then lemma says

$$gcd(287,91) = gcd(91,14)$$

now divide 91 by 14

$$91 = 14 * 6 + 7$$

Then lemma says

$$gcd(91,14) = gcd(14,7)$$

now divide 14 by 7

$$14 = 7 * 2 + 0$$

Thus, $gcd(14,7) = 7$  

Therefore,

$$gcd(287,91) = gcd(91,14) = gcd(14,7) = 7$$

## Extended Euclidian Algorithm

Express $gcd(252,198)$ as $252s + 198t$, for some int $s$ and $t$

$$252 = 198*1+54\tag{1}$$

$$198 = 54*3 +36\tag{2}$$

$$54 = 36*1 +18\tag{3}$$

$$36 = 18*2\tag{4}$$

Hence, $gcd(252,198) = gcd(36,18)=18$  

Rearrange (3) so remainder is the subject

$$18 = 54+(-1)(36)$$

sub in the rearranged (2) into the correct pos at 36

$$= 54+(-1)(198+(-3)(54))$$

simplify

$$=(-1)(198)+4(54)$$

sub in the rearranged (1) into the correct pos at 54

$$=(-1)(198)+4(252+(-1)(198))$$

simplify

$$=4(252)+(-5)(198)$$

Hence,

$$s=4, t=-5$$

$$gcd(252,198) = 252(4) + 198(-5)$$


# Topic 3 Combinatronics

Counting and set theory  

## Important Formulas

$$n_1n_2$$

$$n_1 +n_2$$


$n_1 + n_2$ - (ways common to $n_1$ and $n_2$)

$$|A_1 \cup A_2 |= |A_1| + |A_2| - |A_1 \cap A_2|$$

$$\frac{n}{d}$$

$$_nP_r =\frac{n!}{(n-r)}$$

$\frac{N}{k}$, (round up to closest integer)

## Product Rule

Task1 got $n_1$ ways to do.  
For each way in $n_1$, there are $n_2$ ways to do task2.  
Thus, there are $n_1n_2$ ways to do task1 then task2

Use cases, when positions are limited and cannot repeat positions, e.g. offices/remove from limited pool

## Sum Rule

Task got $n_1$ ways of doing or $n_2$ ways of doing.  
None of $n_1$ is same as $n_2$, i.e. mutually exclusive  
Ways to do task = $n_1 +n_2$

Use case, when only 1 "victor" e.g. elect 1 president. 8 males, 5 females, total options 13

## Subtraction Rule

Task can be done in either $n_1$ or $n_2$ ways or both.  
Ways to do task = $n_1 + n_2$ - (ways common to $n_1$ and $n_2$)  
$$|A_1 \cup A_2 |= |A_1| + |A_2| - |A_1 \cap A_2|$$

use case, total 350, 220 in CS, 147 in business, 51 dual major in CS and business, find non-cs non-business

## Division Rule

Task can be done $n$ ways  
For evey way $w$, there are exactly $d$ ways in $n$ that correspond to way $w$ (basically copies due to conditions)  
Then, there are $\frac{n}{d}$ ways to do the task

use case, conditional sequence, e.g. seating next to specific neightbours at square table  
here you rotate clockwise is new arrangement but still same neighbour

## Permutation

define:  
a permutation of a set of distinct objects is an **ORDERED** arrangement of these objects.  
An ordered arrangement of r elements of a set is called an r-permutation (where $r < len(set)$)

e.g.:  
$S = \{1,2,3\}$

Ordered arrangement $(3,1,2)$ is a permutation of S  
Ordered arrangement $(3,2)$ is a 2-permutation of S  

number of $r$-permutations of a set with $n$ elements is denoted by $P(n,r),\ \ ^nP_r,\ \ _nP_r$
$$_nP_r = n(n-1)(n-2)...(n-r+1)$$
$$=\frac{n!}{(n-r)}$$

$_nP_0=1$ whenever n is a non-negative integer since only one way to order 0 elements

1st 2nd 3rd place, 100 contestants  
how many ways to choose winners  
(can be seen as product rule or as permutations)
$_{100}P_3 = 100*99*98 = 970\ 200$

## Combinations

An $r$-combination of a set is an **UNORDERED** selection of $r$ elements from the set.  
Thus, an $r$-
combination is simply a subset of the set, with the subset having $r$ elements.

$S=\{1,2,3,4\}$
$\{1,3,4\}$ is a 3-combination from $S$
$\{4,1,3\}$ is the **SAME** 3-combination, since unordered

Notation:  
$r$-combinations of a set with $n$ distinct elements is denoted by:  
$C(n,r),\ \ ^nC_r,\ \ _nC_r,\ \ (^n_r)$

Theorem:  
number of $r$-combinations of a set with $n$ elements, where $n$ is a non-negative integer and $r$ is an integer with $0\leq r\leq n$ is
$$_nC_r = \frac{n!}{r!(n-r)!}$$

Corollary  
let $n$ and $r$ be non-negative integers with $r\leq n$  
Then, $_nC_r = _nC_{n-r}$  
Thus,
$$_nC_r = \frac{n!}{r!(n-r)!}$$
$$= _nC_{n-r}$$

## Pigeonhole principle

Theorem:  
If $k+1$ or more objects are placed into $k$ boxes, then there is at least 1 box containing 2 or more objects  

E.g.  
Group of 367 people, must be at least 2 with same birthday, since only 366 possible birthdays  
In any group of 27 English words, must be at least 2 that begin with the same letter

## Generalised Pigeonhole principle

Theorem (generalised Pigeonhole principle):  

If $N$ objects placed into $k$ boxes, then there is at least 1 box containing at least $\lceil\frac{N}{k}\rceil$ objects  
$\lceil\rceil$ is ceiling round, round up to nearest integer

e.g. 6 computers in network, all connected to at least 1 other computer.  
Show there are at least 2 computers that have the same number of connections.  
"Holes" are num connections: 1,2,3,4,5  
"Pigeons" are computers  
$N=6,\ k=5$  
$\lceil\frac{6}{5}\rceil=2$

e.g. How many students in class to ensure 6 students get same grade out of (A,B,C,D or F)  
$\lceil\frac{N}{5}\rceil=6$  
$6\leq\lceil\frac{N}{5}\rceil<\frac{N}{5}+1$  
$6\leq\frac{N}{5}+1$  
$5\leq\frac{N}{5}$  
$25\leq\N$  
Ans: $26$


# Tutorial 1 
## q1
1a. $\displaystyle\sum_{k=1}^5(k+1)$
1. find num of terms, 
2. write out first few terms if have many
3. determine they type of sequence: in ths case: arithmetic

1b. $\displaystyle\sum_{j=0}^4(-2)^j$
1. mind the index
2. mind lower limit
3. determine if this is a special sequence
geometric

1c. $\displaystyle\sum_{i=0}^10-3$
1. mind the index
2. mind lower limit
3. determine if this is a special sequence
4. in this case is geometric or ????

1d. $\displaystyle\sum_{j=0}^8(2^{j+1}-2^j)$
1. Mind index
2. mind lower limit
3. simplify the summation terms in advance: $2*2^j-2^j = $  
OR  
break up into sum of 2 summations: $\displaystyle\sum_{j=0}^8(2^{j+1}) - \displaystyle\sum_{j=0}^8(-2^j)$
4. determine the secial sequence, in this case: geometric

## q2
1. generate terms one after another (recursive formula)
you can determin it is recusive since you see $a_{n-1}$

## q3
1. use heeuristic approach (list first few terms) for calculation or verification  
1 year: $1000 * (1+7\%)^1$  
2 year: $1000 * (1+7\%)^2$  
3 year: $1000 * (1+7\%)^3$  
4 year: $1000 * (1+7\%)^4$

Compund interest is a geometric sequence.  

## q4
Find the sum of the first n terms of an arithmetic series whose first term is 1 and whose common
difference is 5  
$a_n = a + (n-1)d$  
$a_1 = 1$, $d = 5$  
$S_n = \frac{n(2a + (n-1)d)}{2} = \frac{n(5n-3)}{2}$

## q5

application of general formula and summation equation of arithetic progression
only need know first term and common difference to determin an arithmetic progression

term 7 = 7,  
sum of first 10 terms is 60  
$a_7 = a+6d = 7 $  
$S_{10} = \frac{10(2a+9d)}{2} = 60$  
solve the linear equations with two variables, a=3, d=$\frac{2}{3}$

## q6
min the number of terms
find expression for $2(3) +2(3)^2 + ... +2(3)^n$
is geometric  
first term a = 2, common ratio r = 3
total n+1 terms
$$S_{n+1} = \frac{a(1-r^{n+1})}{1-r} = \frac{2(1-3^{n+1})}{1-3} = 3^{n+1}-1$$

$$S_{n+1} = S_n + a_{n+1} = \frac{a(1-r^n)}{1-r} + a_nr$$

## q7

7a. 
$\displaystyle\sum_{j=0}^8 3*2^j$

$j=0, 3*2^0 = 3$  
$j=1, 3*2^1 = 6$  
$j=2, 3*2^2 = 12$  
actually is geometric prograssion  
a = 3, r = 2

7b.
$\displaystyle\sum_{j=0}^8 (-3^j)$

$j=0, -3^0 = 9$  
$j=1, 3^1 = -27$  
$j=2, 3^2 = 81$  
actually is geometric prograssion  
a = 3, r = 2

7c.
$\displaystyle\sum_{j=4}^10 (2+3j)$  
mind lower limit  
mind number of terms  
$a_j=2*3j$  
$a_{j+1}=2*3{j+1}$  
$a_{j+2}=2*3{j+2}$

actually is arithmetic prograssion

## q8

Mind index  
can directly use summation euation for geometric progression when the number of terms is approching infinity

$a_0 = \frac{1}{2^{2n}} = \frac{1}{2^{2*0}} = 1$
$a_1 = \frac{1}{2^{2n}} = \frac{1}{2^{2*1}} = \frac{1}{4}$

geometric progression, a = 1, r = $\frac{1}{4}$

$$lim_{n->∞} S_n = lim_{n->∞} \frac{a(1-r^n)}{1-r} = lim_{n->∞} \frac{1(1-\frac{1}{4}^n)}{1-\frac{1}{4}} = \frac{4}{3}$$

## example exam qn:  
$$\displaystyle\sum_{j=0}^8 (3*2^j+(2+3j))$$
$$\displaystyle\sum_{j=0}^8(3*2^j) + \displaystyle\sum_{j=0}^8(2+3j)$$

# Tutorial 2

first few qn are about modulo ops  
middle few qn are about prime factorisationn
last few qn is euclidian and exxtended euclidian

## Q1

normal long division to find remainder  
or write out $a=qm+r$ into $r=a\mod{m}$

## Q2

$a≡b\mod{m}$ means
$a\mod{m} = b\mod{m}$
$a=qm+r$
q can be any integer. Thus a can be -42,-15,12,39 or onwards
since have constraint $0\leq a\leq26$

## Q3

Check remainder of both left and right portions of equation.
if remainders do not match, then not congruent

## Q4

Brute forcce each mod in the bracckets first then add the two remainders  
OR  
use modulo arithmetic property (Addition) formula

NOTE, following equation is incorrect application of the addition formula:  
$(-133\mod{23})+(26\mod{23})=(-133+26)\mod{23}$  

$(-133\mod{23})$, remainder is between 0 and 22  
$(26\mod{23})$, remainder is between 0 and 22  
BUT if add both remainders together, may result in value more than 23. so thats why need mod again

it should be:  
$(a+b)\mod{m} = ((a\mod{m})+(b\mod{m}))\mod{m}$

## Q5

Be careful of exponentiation and mutiplication property of modulo arithmetic

## Q6

any composite int will have at least 1 prime number divisor that is $\leq \sqrt{n}$

Can prove if prime by checking if number mod all primes less than $\sqrt{n}$ = 0

## Q7

rather than do normal prime factorisation, you can check for first prime by using the modulo method,  
e.g. 1001 mod 7 = 0  
hence, 1001 = 7 * 143  
then use the modulo method on 143 again to get 11 * 13  
Thus, 1001 = 7 * 11 * 13  

May need to prove all nums are prime  
e.g. 1111 = 11 * 101, need to prove 101 is prime

## Q8

find all **factors** (not prime factors) of each number $n$ from 1 to $n$  
This helps to prove GCD between 2 nums is 1

e.g.  
15: 1,3,5,15  
11: 1,11  
19: 1,19

## Q9

remember, GCD is min power of **common** prime factors  

if number has no prime facctor, can do power 0 to represent easier  
e.g.  
$(3^5 * 5^5)=(2^0 * 3^5 * 5^5)$

## Q10

Prime factorise both numbers  
find gcd and lcm.  
prove with basic math that $gcd(a,b) * lcm(a,b) = ab$

## Q11

normal euclidian algo, just practice application

## Q12

when applying extended euclidian, be careful when simplifying and when making remainder the subject of the equation