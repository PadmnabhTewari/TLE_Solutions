for j in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    if(a==1):
      print(0)
    else:
      ans=[]
      ans.append(l[-1]-l[0])
      for i in range(a-1):
          ans.append(l[i]-l[i+1])
      ans.append(max(l[1:])-l[0])
      ans.append(l[a-1]-min(l[:a-1]))
      print(max(ans)) 
    
    
    
    
