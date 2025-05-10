for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    if(len(s)>=3):
        print("no")
    else:
        l.sort()
        if(abs(l.count(l[0])-l.count(l[len(l)-1]))<=1):
            print("yes")
        else:
            print("no")
        
