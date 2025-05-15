for i in range(int(input())): 
       a=int(input())
       l=list(map(int,input().split()))
       c=0
       p=[]
       p.append(0)
       for i in l:
             if(i==0):
                  c=c+1
                  p.append(c)
             else:
                  c=0
       print(max(p))
 	 	     	 				  		  	 	 				 	
