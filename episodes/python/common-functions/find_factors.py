# from timer import timer
# @timer
def factors(number, unique_values):
    factors = {}
    key = 1
    for i in range(1, number+1):
        if number % i == 0:
            dividend = number / i
            factors[key] = [int(dividend), i]
            key += 1
    if unique_values:
        new_dict = {}
        for key in factors:
            factors[key].sort()
        for key, value in factors.items():
            if value not in new_dict.values():
                new_dict[key] = value
        return new_dict
    else:
        return factors


print(factors(513213, True))

