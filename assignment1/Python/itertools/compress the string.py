# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *

a = input()
for x,y in groupby(map(int,list(a))):
    print(tuple([len(list(y)), x]) ,end = " ")
