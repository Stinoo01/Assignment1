# Enter your code here. Read input from STDIN. Print output to STDOUT
STDIN = int(input())
for x in range(STDIN):
    folklore = input()
    evermore = set(input().split())
    reputation = int(input())
    fearless = set(input().split())
    print(evermore.issubset(fearless))