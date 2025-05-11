for i1 in range(int(input())):
    a,b=map(int, input().split())
    c=input()
    d=input()
    j=0
    for i in range(6):
        if(d in c):
            print(i)
            j=j+1
            break
        c+=c
    if(j==0):    
        print(-1)
