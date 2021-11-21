# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a,b = input().split()
words = list(permutations(a,int(b)))
words = sorted(words, reverse = False)
for x in words:
    print(*x, sep = "")
