import math
for i in range(int(input())):
  a=int(input())
  l=list(map(int,input().split()))
  if(a&1!=0):
    print(4)
    print(1,a)
    print(1,a-1)
    print(a-1,a)
    print(a-1,a)
  else:
    print(2)
    print(1,a)
    print(1,a)
