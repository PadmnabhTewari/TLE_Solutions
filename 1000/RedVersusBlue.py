for i in range(int(input())):
    n,a,b=map(int,input().split())
    s1=a//(b+1)
    s2=a%(b+1)
    s=""
    for i in range(s2):
        s+='R'*(s1+1)
        s+='B'
    for i in range(b-s2):
        s+='R'*(s1)
        s+='B'
    s+='R'*s1
    print(s)
