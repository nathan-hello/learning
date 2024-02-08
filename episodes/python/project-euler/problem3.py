#Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

#NOTE: this is cheating but get out of town why am i going to make a prime factor generator  

import sympy
factor = 600851475143

print(sympy.primefactors(factor)[-1])


