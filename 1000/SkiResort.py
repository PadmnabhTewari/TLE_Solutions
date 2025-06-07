for t in range(int(input())):
    n,k,q=map(int, input().split())
    l1=list(map(int, input().split()))
    m=0
    l2=[]
    for i in l1:
        if(i<=q):
            m+=1
        else:
            if(m>=k):
                l2.append(m)
            m=0
    if (l1[-1]<=q):
        if (m>=k):
            l2.append(m)
    c=0
    if (len(l2)>0):
        for a in l2:
            if (l2==k):
                c+=1
            else:
                c+=((a - k + 1) * (a - k + 2)) // 2
        print(c)
    else:
        print(0)


 
