# Enter your code here. Read input from STDIN. Print output to STDOUT
Folklore = int(input())
Fset = set(map(int, input().split()))
Evermore = int(input())
Eset = set(map(int, input().split()))

Fdef = Fset.difference(Eset)
Edef = Eset.difference(Fset)

output = Fdef.union(Edef)

for i in sorted(list(output)):
    print(i)
