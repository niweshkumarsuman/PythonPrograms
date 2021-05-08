def pattern(n):
      
      for i in range(1,n+1,1):
           for j in range(i,n,1):
               print("*",end=" ")
           for k in range(1,i+1,1):
               print("#",end=" ")
           for p in range(1,i,1):
               print("#",end=" ")
           for l in range(i,n,1):
               print("*",end=" ")
           print()
            
n=int(input("Enter a number:")) 
pattern(n)