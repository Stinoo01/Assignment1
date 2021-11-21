if __name__ == '__main__':
    n = int(input())
    student_mark = {}
    for _ in range(n):
        name, *line = input().split()
        score = list(map(float, line))
        student_mark[name] = score
    query_name = input()
    mark = 0
    for x in student_mark[query_name]:
        mark=mark+x 
    result=mark/3
    print("%.2f"%result)
