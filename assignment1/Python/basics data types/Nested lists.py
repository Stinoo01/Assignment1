list1=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])

grades_list=sorted(list(set([student[1] for student in list1])))
second_grade=grades_list[1]

student_second=[
    student
    for student in list1
    if student[1]==second_grade
]

student_second.sort()
for student in student_second:
    print(student[0])