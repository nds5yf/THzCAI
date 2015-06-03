import math 

x = input('Select a height: ')
y = input('Select a width: ')


area = x * y
size = math.pow(2, area)



bn = '{0:0' + str(area) + 'b}'

top = 0
li = []
while top < size:
    
    mask = bn.format(top)
    li.append(mask)
    top = top + 1

print li
