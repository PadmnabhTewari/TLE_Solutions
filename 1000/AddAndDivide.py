for i in range(int(input())):
    a,b=map(int,input().split())
    m=a+1 
    if(b==1):
        l=1
    else:
        l=0
    for i in range(l,100):
        j=b+i
        x=a
        while x>0:
            i=i+1
            x=x//j
        m=min(m,i) 
    print(m)
