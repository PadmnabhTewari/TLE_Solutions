for i in range(int(input())):
    a=int(input())
    l=list(map(int, input().split()))
    if(len(l)==l.count(l[0])):
        print(-1)
        continue
    m=min(l)
    b=[m]*l.count(m)
    c=[]
    for i in l:
        if(i!=m):
            c.append(i)
    print(len(b),len(c))
    print(*b)
    print(*c)
