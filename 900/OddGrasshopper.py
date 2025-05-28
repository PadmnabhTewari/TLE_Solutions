for i in range(int(input())):
    a,b=map(int, input().split())
    d=0
    if(b%4==0):
        d=0
    elif(b%4==1):
        d=-b
    elif(b%4==2):
        d=1
    else:
        d=b+1
    if(a%2==0):
        print(a+d)
    else:
        print(a-d)
