for k in range(int(input())):
    n=int(input())
    l1=[]
    l2=[]
    if n==1:
        m=int(input())
        l=list(map(int,input().split()))
        l.sort()
        print(l[0]) 
    else:
        for u in range(n):
            m=int(input())
            l=list(map(int,input().split()))
            l.sort()
            l2.append(l)
            l1.append((l[1],u))
        l1.sort()
        p=l1[0][1]
        s=0
        for i in range(len(l2)):
            if i!=p:
                s+=l2[i][1]
        o=l2[p]
        for u in range(len(l2)):
            if u!=p:
                o.append(l2[u][0])
        s+=min(o)
        print(s)

        
            
            
            
