# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

n = int(input())
scol = ','.join(input().split())
Student = collections.namedtuple('Student',scol)
'''
here same problem: hackerrank takes MARK and my python does not
'''
sum = 0
for x in range(n):
    row = input().split()
    student = Student(*row)
    sum += int(student.MARKS)

a = sum/n
print(a)
