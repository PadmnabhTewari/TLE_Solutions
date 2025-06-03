for j in range(int(input())):
  n=int(input())
  arr=list(map(int,input().split()))
  ans=-1 
  for i in range(1,n-1):
    if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
      ans=i 
      break 
  if(ans==-1):
    print("NO")
  else:
    print("YES")
    print(i,i+1,i+2)
