L1=[]
n=int(input("Enter the number of element"))
print("Enter the Elements")
for x in range(0,n,1):
    n1=int(input())
    L1.append(n1)
print(L1)
print("Enter the position")
p=int(input())
print("Enter value")
v=int(input())
L1.insert(p,v)
print(L1)