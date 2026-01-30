#Vẽ tam giác
T=int(input())
if T<=100:
 for i in range(T):
   n = int(input())
   sao = "* "
   for i in range(1,n+1):
       print(sao*i)
   i=n-1
   while 0<i<n:
       print(sao*i)
       i=i-1
        
            
          
            
    
    
    