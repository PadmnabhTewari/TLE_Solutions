for i in range(int(input())):
    a=int(input())
    c2=0
    c3=0
    while(a%2==0):
        a//=2
        c2+=1
    while(a%3==0):
        a//=3
        c3+=1
    if(a==1 and c2<=c3):
        print(2*c3-c2)
    else:
        print(-1)
