for i in range(int(input())):
    m,k=map(int,input().split())
    a=list(map(int,input().split()))
    mn=10000
    c=0
    for i in range(m):
        r=(a[i]+k-1)//k
        mn=min(mn,r*k-a[i])
        if(a[i]%2==0):
            c+=1
    if(k==4):
        mn=min(mn, max(0, 2 - c))
    print(mn)
 
