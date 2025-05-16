for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    t=0
    for i in l:
        t=t^i
    if(a%2==0):
        if(t==0):
            print(max(l))
        else:
            print(-1)
    else:
        print(t)
