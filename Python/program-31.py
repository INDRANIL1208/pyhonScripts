k=1
for r in range (0,4,1):
    print(" "*(3-r),end='')
    for c in range (0,2*r+1,1):
        if (c%2==0):
            print(k,end='')
        else:
            print(" ",end='')
    k=k+2
    print(" "*(3-r))