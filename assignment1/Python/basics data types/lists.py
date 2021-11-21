if __name__ == '__main__':
    N = int(input())
    list_=[]
for x in range(N):
    k = input().split(" ")
    command= k[0]
    if command=="insert":
        list_.insert(int(k[1]), int(k[2]))
    if command=="remove":
        list_.remove(int(k[1]))
    if command=="append":
        list_.append(int(k[1]))
    if command=="sort":
        list_.sort()
    if command=="reverse":
        list_.reverse()
    if command=="pop":
        if (len(list_)!=0):
            list_.pop()
    if command=="print":
        print(list_)
