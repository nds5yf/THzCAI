import math 

x = input('Enter n for 2^n: ')

dim = math.pow(2, x)



#Matrices' lists start top left to bottom right.



def invert(string):
    inv = ""
    for j in range (0, len(string)):    
        if string[j] == '0':
            inv+='1'
        else:
            inv+='0'
    return inv

def hadamard(integer, string):
#Global List for masks
    li = []
#Base Case for recursion
    if integer == 1:
        return li
#Recursive Case
    else:
        s = ""
        if:
           s+=string
           s+=string
           s+=string
           s+=invert(string)
           li.append(s)
        elif:
           s+=string
           s+=string
           s+=invert(string)
           s+=string
           li.append(s)
        elif: 
           s+=string
           s+=invert(string)
           s+=string
           s+=string
           li.append(s)
        elif: 
           s+=invert(string)
           s+=string
           s+=string
           s+=string
           li.append(s)
        hadamard(integer - 1, s)
     