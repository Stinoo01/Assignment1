# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

ctr = Counter(input() for x in range(int(input())))
print(len(ctr))
print(*ctr.values())
