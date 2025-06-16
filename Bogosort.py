for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    l.sort()
    l.reverse()
    print(*l)
