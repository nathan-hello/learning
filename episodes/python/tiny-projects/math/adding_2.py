total_adds = []
loop_cycle = True

def add_func(int):
    total_adds.append(int)
    total_sums = sum(total_adds)
    return total_sums

def check_input_type(check_int):
    try:
        user_check = float(check_int)
        add_func(user_check)
    except ValueError:
        global loop_cycle
        loop_cycle = False

def whileloop():
    while loop_cycle == True:
        user_input = input("enter numbers until you don't feel like it: ")
        check_input_type(user_input)
        
        if loop_cycle == False:
            print("Sum of digits entered =", add_func(0))
            break
        
whileloop()


