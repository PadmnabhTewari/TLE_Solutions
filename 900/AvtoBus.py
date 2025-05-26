for i in range(int(input())):
    a=int(input())
    if(a%2!=0):
        print(-1)
    else:
        n=a//2
        if(n==1):
          print(-1)
          continue
        if(n%3!=0):
          print((n//3)+1,end=" ")
        else:
          print(n//3,end=" ")
        print(n//2)
