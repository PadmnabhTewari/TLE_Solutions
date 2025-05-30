for j in range(int(input())):
    s=input()
    n=len(s)
    res=0
    for i in range(n-1):
        for j in range(i+1,n):
            if(int(s[i]+s[j])%25==0):
                res=n-i-2
    print(res)
