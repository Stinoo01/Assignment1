# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import*
a = int(input())
b = OrderedDict()
for x in range(a):
    item = input().split()
    itemPrice = int(item[-1])
    itemName = " ".join(item[:-1])
    if(b.get(itemName)):
        b[itemName] += itemPrice
    else:
        b[itemName] = itemPrice
for x in b.keys():
    print(x, b[x])

