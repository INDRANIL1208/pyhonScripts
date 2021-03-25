n1=int(input("Enter a number in decimal"))
L1=[]
while(n1>0):
    L1.append(n1%2)
    n1=n1//2
L1.reverse()
print(L1)