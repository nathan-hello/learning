def accumulate(x, y):
    accumulated = int(x) + int(y)
    return accumulated
def inputting():
    for_break = "y"
    while for_break == "y":
        x = input("Enter a number: ")
        y = input("Enter a number: ")
        accumulated = accumulate(x, y)
        print(accumulated)
        for_break = input("Do you want to add another number? y/n " )
    if for_break == "n":
        print("of course you do!")
        for_break = "y"
        inputting()
    else:
        print("Fine have it your way") 
inputting()