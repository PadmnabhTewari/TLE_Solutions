for i in range(int(input())):
    n,k,x = map(int,input().split())

    if (2*x >= (k*(k+1)) and 2*x <= (2*k*n+k-k*k)):
        print("YES")
    else:
        print("NO")      
