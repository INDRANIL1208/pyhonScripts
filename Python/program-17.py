s=0
for y in range (1,12,1):
    m=1
    for x in range (1,y+1,1):
        m=m*x
        print(s,'+',m,'=',end='')
        s=s+m
    print(s)
