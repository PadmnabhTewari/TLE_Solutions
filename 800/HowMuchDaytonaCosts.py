for i in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    if(b in l):
        print("YES")
    else:
        print("NO")
