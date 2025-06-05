for i in range(int(input())):
    n,p=map(int, input().split())
    l1=list(map(int, input().split()))
    l2=list(map(int, input().split()))
    l3=[]
    m=n
    for i in range(n):
        l3.append([l1[i],l2[i]])
    l3.sort(key=lambda x: (x[1], -x[0]))
    sum=p
    x=0
    i=0
    m-=1
    while m>0 and i<n:
        if l3[i][1] > p:
            print(sum+m*p)
            x=x+1
            break

        if m>l3[i][0]:
            sum+=(l3[i][1]*l3[i][0])
        else:
            sum+=l3[i][1]*m
        m=m-l3[i][0]
        i += 1
    if(x==0):
        print(sum)
