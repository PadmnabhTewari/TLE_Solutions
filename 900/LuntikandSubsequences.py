for i in range(int(input())):
    a=int(input())
    l=list(input().split())
    o=l.count('0')
    z=l.count('1')
    b=2**(o)
    print(b*z)
