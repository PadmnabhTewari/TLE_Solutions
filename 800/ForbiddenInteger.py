for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if c!=1:
        print('YES')
        print(a)
        print('1 '*a)
    elif a%2==0 and b>=2 and c!=2:
        print('YES')
        print(a//2)
        print('2 '*(a//2))
    elif a>=3 and b>=3 and c!=1 and c!=2:
        print('YES')
        print(a//2+1)
        print('1',end=' ')
        print('2 '*(a//2))
    elif a>=3 and b>=3 and c!=3 and c!=2:
        print('YES')
        print(a//2)
        print('3',end=' ')
        print('2 '*(a//2-1))
    else:
        print('NO')
