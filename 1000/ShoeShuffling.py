from math import *
for _ in range(int(input())):
        n = int(input())
        l1 = list(map(int,input().split()))
        p = [i + 1 for i in range(n)]
        l, r = 0, 0
        ans = True

        while r < n:
            while r < n - 1 and l1[r] == l1[r + 1]:
                r += 1
            if l == r:
                ans = False
            else:
                temp = p[l:r + 1]
                for i in range(r - l):
                    p[l + i] = temp[i + 1]
                p[r] = temp[0]
            l = r + 1
            r += 1
        if ans:
            print(*p)
        else:
            print(-1)
