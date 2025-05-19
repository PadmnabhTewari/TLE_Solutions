from collections import Counter
for i in range(int(input())):
    a,b=map(int,input().split())
    s=input()
    d=Counter(s)
    c=-1
    for j in d:
        if(d[j]%2!=0):
            c=c+1
    if(c<=b):
        print('YES')
    else:
        print('NO')
