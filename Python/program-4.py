c1=0
n=int(input("Enter a number"))
for x in range(1,n+1,1):
 if(n%x==0):
     c1+=1
if (c1==2):
   print("The number is Prime")
else:
  print("The Number is Composite")    