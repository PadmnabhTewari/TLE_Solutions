for i in range(int(input())):
    l=int(input())
    s = input()
    a=0
    c=0
    for j in range(len(s)):
        if(s[j]==')'):
            c=c+1
        else:
            c=c-1
        a=max(a,c)
    print(a)
