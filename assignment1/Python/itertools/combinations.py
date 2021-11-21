# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
a,b = input().split()

for x in range(1, int(b)+1):
    for y in combinations(sorted(a), x):
        print("".join(y))  