for i in range(int(input())):
    b=int(input())
    s=input()
    c=1
    mc=1
    for j in range(1,b):
        if(s[j]==s[j-1]):
            c=c+1
        else:
            if(c>mc):
                mc=c
            c=1
    print(max(c,mc)+1)
        
