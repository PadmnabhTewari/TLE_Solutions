for i in range(int(input())):
    a,b=list(map(int,input().split()))
    l=list(map(int,input().split()))
    l.sort()
    count=[]
    m=0
    j=m+1
    while(j<=a-1):
        if(abs(l[j-1]-l[j])>b):
          count.append(j-m)
          m=j
          j=m+1
        else:
          j=j+1   
    if(j==a):
        count.append(j-m)
    c=max(count)
    print(a-c)
