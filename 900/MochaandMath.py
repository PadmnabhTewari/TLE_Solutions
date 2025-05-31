for i in range(int(input())):
    a=int(input())
    l=list(map(int, input().split()))
    b=l[0]
    for i in range(a):
        b=b&l[i]
    print(b)
