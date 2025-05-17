for i in range(int(input())):
    a=int(input())
    l=[0]+list(map(int,input().split()))
    p=1
    c=0
    for j in range(2,a+1):
        if(l[j]%2==l[j-1]%2):
            c=c+1
    print(c)
