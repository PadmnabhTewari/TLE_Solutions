l=[]
for i in range(1,100):
    l.append(2**i)
for i in range(int(input())):
    a=int(input())
    if(a in l):
        print("No")
    else:
        print("Yes")
