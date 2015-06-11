#Automation for Matrix Generation
#Michael Eller mbe9a
#Noah Sauber nds5yf
#THzCAI
#09 June 2015

import math

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

#gets every string in a list and returns it as one long string
#will be used to store the full matrix in the final list
def getMatrix(li):
    string = ""
    for x in range(0, len(li)):
        string += li[x]
    return string

#simply turn 0's to 1's and vice versa
def inverse(s):
    string = ""
    for x in range(0, len(s)):
        if s[x] == '0':
            string += '1'
        else:
            string += '0'
    return string
   
#rotating the h matrix to create the different combos 
def shift(s, n):
    temp = s
    for i in range (0, n):
        x = len(temp)/4
        l = len(temp)
        string = temp[l - x:] + temp[:l - x]
        temp = string
    return string

#create Hadamard matrices
#'o' should be '0001' or some permutation on the initial call
#'n' is depth of recursion 0 = nothing 1 = 2x2 2 = 4x4 etc...
#'m' should be exactly n + 1.
def hadamard(n, o, m, rlist):
    s = ""
    if n == 0:
        return rlist
         
    rlist.append(o)
    rlist.append(shift(o, 1))
    rlist.append(shift(o, 2))
    rlist.append(shift(o, 3))
    
    s = o
    s += o
    s += o
    s += inverse(o)
    rlist = hadamard(n - 1, s, m, rlist)
    
    o = shift(o, 1)
    
    rlist.append(o)
    rlist.append(shift(o, 1))
    rlist.append(shift(o, 2))
    rlist.append(shift(o, 3))
    
    s = o
    s += o
    s += o
    s += inverse(o)
    rlist = hadamard(n - 1, s, m, rlist)
    
    o = shift(o, 1)
    
    rlist.append(o)
    rlist.append(shift(o, 1))
    rlist.append(shift(o, 2))
    rlist.append(shift(o, 3))
    
    s = o
    s += o
    s += o
    s += inverse(o)
    rlist = hadamard(n - 1, s, m, rlist)
    
    o = shift(o, 1)
    
    rlist.append(o)
    rlist.append(shift(o, 1))
    rlist.append(shift(o, 2))
    rlist.append(shift(o, 3))
    
    s = o
    s += o
    s += o
    s += inverse(o)
    rlist = hadamard(n - 1, s, m, rlist)

    rlist = list(set(rlist))
    
    li = []
    for x in range(0, len(rlist)):
        if len(rlist[x]) < (1 + math.pow(2, m)):
            li.append(rlist[x])

    for x in range (0, len(li)):
        rlist.remove(li[x])
        
    
    return rlist
    
print hadamard(3, '0001', 4, [])
       