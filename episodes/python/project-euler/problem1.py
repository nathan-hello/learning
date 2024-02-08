#Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

max_count = 1000
first_dividend = 3
second_dividend = 5
# div_list = []



div_count = 0
for x in range(max_count):
    if x % first_dividend == 0:
        print(f'{x} HIT')
        div_count += x
        # div_list.append(x)
    if x % second_dividend == 0:
        # div_list.append(x)
        div_count += x
        print(f'{x} HIT')
    else:
        print(x)
# print(sum(div_list))
print(div_count)


