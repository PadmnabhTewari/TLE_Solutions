for i in range(int(input())):
    a,b=map(int,input().split())
    m=abs(a-b)
    if(a==b):
        print("0 0")
    else:
        c=min(a%m,m-a%m)
        print(m,c)
