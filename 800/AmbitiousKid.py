a=int(input())
l=list(map(int,input().split()))
if(0 in l):
    print(0)
    exit()
m=abs(l[0])
for j in range(a):
    if(m>abs(l[j])):
        m=abs(l[j])
print(m)
