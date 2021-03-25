r1=int(input("Enter the lower limit of the 'Range\'"))
r2=int(input("Enter the upper limit of the 'Range\'"))
print ("The prime numbers are")
for x in range(r1,r2+1,1):
    c=0
    for y in range(1,x+1,1):
        if(x%y==0):
            c=c+1
    if(c==2):
         print(x,end=' ')