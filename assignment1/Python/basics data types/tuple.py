if __name__ == '__main__':
    n = int(input())
    _list = map(int, input().split())
    t=tuple(_list)
    print(hash(t))