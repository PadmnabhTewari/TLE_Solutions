for i in range(int(input())):
    n, a, b = list(map(int, input().split()))
    if(n==a==b or n-(a+b)>=2):
        print("YES")
    else:
        print("NO")
