t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    p=l[:]
    p.sort()
    
    if p==l:
        print("YES")
    else:
        if k>=n:
            print("YES")
        elif (k==1 or k==0) and n>1:
            print("NO")
        else:
            print("YES")
