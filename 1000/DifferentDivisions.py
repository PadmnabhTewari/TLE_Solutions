def prime(n):
    if(n<=1):
        return False
    i=2
    while(i*i<=n):
        if(n%i==0):
            return False
        i=i+1
    return True
for _ in range(int(input())):
    n=int(input())
    a,b=0,0
    for i in range(1+n,10000000,1):
        if(prime(i)):
            a=i
            break
    for i in range(a+n,1000000,1):
        if(prime(i)):
            b=i
            break
    print(a*b)
