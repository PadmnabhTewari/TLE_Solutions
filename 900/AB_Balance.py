for i in range(int(input())):
    s=input()
    a=len(s)
    if(s[0]==s[a-1]):
        print(s)
    else:
        print(s[:a-1]+s[0])
