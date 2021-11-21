# Enter your code here. Read input from STDIN. Print output to STDOUT
country = int(input())
country_list = set()
for x in range(country):
    country_list.add(input())

print(len(country_list))
