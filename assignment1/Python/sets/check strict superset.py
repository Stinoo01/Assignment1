# Enter your code here. Read input from STDIN. Print output to STDOUT
t = set(input().split())
input_ = int(input())
output = True

for x in range(input_):
    t2 = set(input().split())
    if not t2.issubset(t):
        output = False
    if len(t2) >= len(t):
        output = False

print(output)