for i in range(int(input())):
    a=int(input())
    c=0
    for j in range(1,a+1):
        if(a%j!=0):
            c=j
            break
    if(c==0):
        print(a)
    else:
        print(c-1)
