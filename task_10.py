def take_common(arg1,arg2):
    common_list = []
    for x in arg1:
        if x in arg2:
            common_list.append(x)
    print ("Common letters: " + ", ".join(set(common_list)))


take_common('boss','baby')