print('The Even Numbers are',end=' ')
for x in range(1,101,1):
   if (x%2==0):
    if(x<100):
     print(x,end=',')
    else: 
      print(x,end='.')  