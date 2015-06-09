#Automation for Matrix Generation
#Michael Eller mbe9a
#THzCAI
#09 June 2015

import math

#checks if the number is a power of 2
#required for Hadamard matrices

def modCheck(n):
    x = n
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 != 0:
        return False
    elif n % 2 == 0:
        x = n / 2
        return modCheck(x)

'''        
x = input ("Input: ")
print modCheck(x)
'''

'''
#Generate binary combinations: all representations of an NxN matrix
# represented as a binary string in the list 'li'
x = input("input the matrix dimension: ")
area = x * x
size = math.pow(2, area)

bn = '{0:0' + str(area) + 'b}'

top = 0
li = []
canvasSize = 900

while top < size:
    
    mask = bn.format(top)
    li.append(mask)
    top += 1
'''

def inverse(s):
    string = ""
    for x in range(0, len(s)):
        if s[x] == '0':
            string += '1'
        else:
            string += '0'
    return string


s = input("Input string: ")
print inverse(s)


#def hadamard(n, depth):
     