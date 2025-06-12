l=[0]*(3*10**5 +1);
x=0;
for i in range(3*10**5 +1):
    x=x^i;
    l[i]=x;
for t in range(int(input())):
    a,b=map(int,input().split())
    x1=l[a-1];
    if x1==b:
        print(a)
    else:
        x1^=b
        if x1==a:
            print(a+2);
        else:
            print(a+1);M
