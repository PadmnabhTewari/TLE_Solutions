from math import *
for _ in range(int(input())):
        x, y = (i for i in input().split())
        str1 = input()
        str2 = str1 + str1
        c = 0
        ma = 0
        for i in str2:
            if (c == 0 and i != y):
                continue
            elif (c != 0 and i != 'g') or i == y:
                c += 1
            elif (i == 'g'):
                ma = max(ma, c)
                c = 0
        print(ma)
