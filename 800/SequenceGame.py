for i in range(int(input())):
    a,b=int(input()), list(map(int, input().split()))
    l=[b[0]]
    for x in range(1,a):
        if(b[x]>=b[x-1]): 
            l.append(b[x])
        else:
            l.append(1)
            l.append(b[x])
    print(len(l))
    print(*l)
