def highest_number(*args):
    high_num = 0
    for num in args:
        if num > high_num:
            high_num = num
    return high_num

print (highest_number(100, 250, 786, 5, 700, 32, 350))