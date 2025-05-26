for i in range(int(input())):
    a=int(input())
    l=[0]
    l1=list(map(int, input().split()))
    l=l+l1
    c=0
    for j in range(a):
        if(l[j+1]>l[j] and l[j]==0):
            c=c+1
    if(c>2):
        print(2)
    else:
        print(c)
