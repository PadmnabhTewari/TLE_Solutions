for i in range(int(input())):
    b=int(input())
    a=list(map(int, input().split()))
    for j in range(b):
        if(j==0):
            if(a[j]==1):
                a[j]+=1
        else:
            if(a[j]==1):
                a[j]+=1
            while(a[j]%a[j-1]==0):
                a[j]+=1
    print(*a)
