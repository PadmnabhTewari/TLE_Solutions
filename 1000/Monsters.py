for i in range(int(input())):
    n,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=[]
    for l in range(n):
        if l1[l] % k == 0:
            l2.append((k,l+1))
        else:
            l2.append((l1[l]%k,l+1))
    ans =sorted(l2,key=lambda x:(-x[0],x[1]))
    res=[]
    for x, y in ans:
        print(y,end=" ")
    print()
