import bisect
l=[]
for i in range(1,10):
    l.append(i)
    l.append(i*10)
    l.append(i*100)
    l.append(i * 1000)
    l.append(i * 10000)
    l.append(i * 100000)
    l.append(i * 1000000)
l.sort()
for i in range(int(input())):
    n=int(input())
    print(bisect.bisect_right(l,n))
