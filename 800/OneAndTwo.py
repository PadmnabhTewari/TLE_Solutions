for i1 in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    c=l.count(2)
    if(c%2):
        ans=-1
    else:
        c=c//2
        for i in range(a):
            if(l[i]==2):
                c=c-1
            if(c==0):
                ans=i+1
                break
    print(ans)
