for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    l2=[]
    c=0
    for j in range(1,a):
        if(l[j-1]>l[j]):
            c=1
            break
        else:
            l2.append(abs(l[j-1]-l[j]))
    if(c==1):
        print(0)
    else:
        print(min(l2)//2+1)
