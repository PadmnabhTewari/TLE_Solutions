for i in range(int(input())):
    a=int(input())
    l=list(map(int, input().split()))
    n=l.count(-1)
    p=a-n
    if(p>=n):
        if n%2==0:
            print(0)
        else:
            print(1)
    else:
        ans=n-p
        ans=(ans+1)//2
        n=n-ans
        if(n%2==0):
            print(ans)
        else:
            print(1+ans)
