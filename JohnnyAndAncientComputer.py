for _ in range(int(input())):
    a,b=sorted(map(int, input().split()))
    k = bin(b//a)[3:]
    if b%a or '1' in k: 
        print(-1)
    else:
        print((len(k)+2)//3)
