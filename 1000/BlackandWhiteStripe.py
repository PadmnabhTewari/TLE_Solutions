for i in range(int(input())):
    a,b=map(int,input().split())
    s=input()
    p=[0]*a
    if(s[0]=='W'):
        p[0]=p[0]+1 
    for i in range(1,a):
        p[i]=p[i]+p[i-1]
        if(s[i]=='W'):
            p[i]=p[i]+1
    ans=float('inf')
    for i in range(a):
        l=i+b-1
        if (l>=a):
            break
        q=p[l]
        if i-1>=0:
            q=q-p[i-1]
        ans=min(ans,q)
    print(ans)


		 	  	 	  							 					     		
