#Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#NOTE: answer is 232792560, if you print each success to screen it will take forever so don't


def func():
    divisors = [x for x in range(20)]
    divisors.pop(0)
    divisors.pop(0)
    dividend = 0
    quotient_score = 1
    
    while True:
        dividend += 1
        for each_divisor in divisors:
            if dividend % each_divisor != 0:
                quotient_score = 1
                break
            else:
                quotient_score += 1
                # print(f'{dividend} is divisible by {each_divisor}, quotient score is {quotient_score}')
        if quotient_score == divisors[-1]:
            return dividend
                

print(func())