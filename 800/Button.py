for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(c%2==1):
        a+=1
        c-=1
    if(a<=b):
        print('Second')
    else:
        print('First')
