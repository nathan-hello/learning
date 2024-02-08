#Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# import time
# start_time = time.time()

def pal_check(n):
    pal_list = []
    first_half, sec_half = [], []
    y = 0
    for x in str(n):
        pal_list.append(x)
    pal_len = len(pal_list)
    if pal_len % 2 == 0:
        for x in range(pal_len):
            if x < pal_len / 2:
                first_half.append(pal_list[x])
            if x >= pal_len / 2:
                sec_half.append(pal_list[x])
        sec_half.reverse()
        if first_half == sec_half:
            return True
    else:
        return False

max_digit = 999
full_list = []
for n in range(max_digit*max_digit):
    if pal_check(n):
        print(f'{n} is a palindrome!')
        full_list.append(n)
    # else:
    #     print(f'{n} is not a palindrome!')
print(f'{full_list[-1]} is the largest palindrome!')

# finish_time = time.time()
# elapsed_time =  finish_time - start_time
# print(elapsed_time)

