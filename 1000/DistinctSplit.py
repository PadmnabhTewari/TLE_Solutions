for _ in range(int(input())):
    n = int(input())
    a = input()
    dp1=[0]*n
    dp2=[0]*n
    dp3={0}
    for i in range(n):
        dp3.add(a[i])
        dp1[i]=len(dp3)-1

    dp4={0}
    for i in range(n-1,-1,-1):
        dp4.add(a[i])
        dp2[i]=len(dp4)-1
    ma=0
    for i in range(n-1):
        if(dp1[i]+dp2[i+1]>ma):
            ma=dp1[i]+dp2[i+1]
    print(ma)


 
