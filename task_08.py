def time_conv(time):
    hrs = time // 60
    min = time % 60 
    if hrs == 1 and min == 1:
        print(f"{hrs} hour, {min} minute")
    elif hrs == 1 and min > 1:
        print(f"{hrs} hour, {min} minutes")
    elif hrs >= 2 and min == 1:
        print(f"{hrs} hours, {min} minute")
    elif hrs == 0 and min == 1:
        print(f"{min} minute")
    elif hrs == 0: 
        print(f"{min} minutes")     
    elif min == 0 and hrs == 1:
        print(f"{hrs} hour")
    elif min == 0:
        print(f"{hrs} hours")     
    else:
        print(f"{hrs} hours, {min} minutes") 

time_conv(120)       