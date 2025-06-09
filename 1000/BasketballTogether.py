n, q = map(int, input().split())
l = list(map(int, input().split()))
c1= 0
j = 0
l.sort(reverse=True)
while n > 0:
    c = l[j]
    i = 0
    while q >= c * i:
        i += 1
        n -= 1
    if n >= 0:
        c1 += 1
    else:
        break
    j += 1
print(c1)
