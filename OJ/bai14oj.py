#Giai thừa kép
n=int(input())
if -1<=n<=30:
  if n==0 or n==1:
      print("1")   
  elif 2<=n:
      if n%2==0:
        mysum = int(1)
        for i in range (2,n+1,2):
          mysum *= i
        print(mysum)
      if n%2!=0:
        mysum = int(1)
        for i in range (3,n+1,2):
          mysum *= i
        print(mysum)
        
            
          
            
    
    
    