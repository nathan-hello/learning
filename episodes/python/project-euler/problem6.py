#Problem 6
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

squared_list, num_list = [], []


for number in range(101):
    squared_num = number * number
    squared_list.append(squared_num)
    num_list.append(number)

sq = sum(squared_list)
num = sum(num_list) * sum(num_list)

answer = num - sq

# print(squared_list, sum_of_nums)
print(answer)

