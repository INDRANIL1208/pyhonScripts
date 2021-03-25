s=0
for y in range (1,12,2):
    m=1
    for x in range (1,y+1,1):
        m=m*x
        n=(y+1)**100
        p=m/n
        s=s+p
print(s)