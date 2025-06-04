for i1 in range(int(input())):
    s=input()
    c=[0,0]
    for i in range(len(s)):
        c[int(s[i])]+=1
    for i in range(len(s)+1):
        if (i==len(s) or c[1-int(s[i])]==0):
            print(len(s)-i)
            break
        c[1-int(s[i])]-=1
