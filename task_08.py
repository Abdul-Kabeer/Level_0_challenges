def time_conv(time):
    hrs = time // 60
    min = time % 60 
    if hrs == 1 and min == 1:
        print(f"{hrs} hour, {min} minute")
    elif hrs == 1 and min >= 0:
        print(f"{hrs} hour, {min} minutes")
    elif hrs >= 0 and min == 1:
        print(f"{hrs} hrs, {min} minute")
    else:
        print(f"{hrs} hrs, {min} minutes")

time_conv(120)        