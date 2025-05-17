for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if(len(set(l))==1):
        print("NO")
    else:
        print("YES")
        l.sort()
        x=l[-1]
        y=l[0]
        l.remove(l[0])
        l.remove(l[-1])
        l.insert(0,x)
        l.insert(1,y)
        print(*l)
