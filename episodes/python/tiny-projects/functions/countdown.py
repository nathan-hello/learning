def counting(countdown):
    print_tuple = iter(countdown)
    for_loop_passes = (len(countdown))

    while for_loop_passes > 0:
        print(next(print_tuple))
        for_loop_passes = for_loop_passes - 1


x = ("apple", "banana", "cherry")
y = ("lemon", "orange", "pastrami")
counting(x)
counting(y)