for _ in range(int(input())):
    s=0
    for i in range(10):
        l=input()
        for j in range(10):
            if(l[j]=='X'):
                s=s+(min(i,j,9-i,9-j)+1)
    print(s)
