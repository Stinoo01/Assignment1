# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
a = int(input())
b = deque()
for x in range(a):
    lst = list(input().split())
    if lst[0]=='append':
        b.append(int(lst[1]))
    elif lst[0]=='appendleft':
        b.appendleft(int(lst[1]))
    elif lst[0]=='popleft':
        b.popleft()
    elif lst[0]=='pop':
        b.pop()
for k in b:
    print(k,end=" ")

