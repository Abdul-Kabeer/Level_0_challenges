#This program will print the common letters in two strings.
a = ("drum") 
b = ("roll")

def extract_common(colist):
    comlist = []
    for x in colist:
        if x in a and b:
            comlist.append(x)
            print ("Common Letters are: " + ", ".join(set(comlist)))
            
extract_common(a and b)