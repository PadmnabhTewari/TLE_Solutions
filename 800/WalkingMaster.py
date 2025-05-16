for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    if(d<b or a+d-b-c<0):
        print(-1)
    else:
        print(d-b+abs(a+d-b-c))
