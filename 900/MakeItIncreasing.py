for j in range(int(input())):
    a=int(input())
    l=list(map(int, input().split()))
    c=0
    d=0
    for i in range(a-1,0,-1):
        if(l[i]==0):
            print(-1)
            d=d+1
            break
        while(l[i-1]>0 and l[i]<=l[i-1]):
            l[i-1]=l[i-1]//2
            c=c+1
    if(d==0):
        print(c)
