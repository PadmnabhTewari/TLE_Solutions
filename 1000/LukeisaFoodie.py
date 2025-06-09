from math import *
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    mn = []
    mx = []
    co = 0
    for i in a:
        mn.append(i - q)
        mx.append(i + q)
    imn = mn[0]
    imx = mx[0]
    for i in range(1, n):
        if imn > mx[i] or imx < mn[i]:
            co += 1
            imn = mn[i]
            imx = mx[i]
        else:
            imn = max(mn[i], imn)
            imx = min(mx[i], imx)
    print(co)
