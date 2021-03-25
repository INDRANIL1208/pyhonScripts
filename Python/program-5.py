print("The prime numbers are")
for y in range(1,101,1):
    c=0
    for x in range(1,y+1,1):
        if(y%x==0):
            c+=1
    if(c==2):
        print(x,end=' ')