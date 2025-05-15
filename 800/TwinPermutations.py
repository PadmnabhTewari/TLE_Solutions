for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    for i in range(a):
        print(a-l[i]+1,end=" ")
    print()
