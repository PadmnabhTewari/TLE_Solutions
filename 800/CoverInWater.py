for i in range(int(input())):
    a=int(input())
    b=input()
    i=0
    c=0
    d=0
    for x in b:
        if(x=='.'):
            i+=1
            c+=1
        else:
            i=0
        if(i==3):
            d=d+1
    if(d>0):
        print(2)
    else:
        print(c)
