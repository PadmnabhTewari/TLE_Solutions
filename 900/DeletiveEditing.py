for i in range(int(input())):
    a,b=map(str,input().split())
    f=0
    for c in a[::-1]:
        if(c==b[-1]):
            b=b[:-1]
        elif(c in b):
            f=1
            break
        if(not b):
            break
    if(b or f):
      print('NO')
    else:
      print('YES')
