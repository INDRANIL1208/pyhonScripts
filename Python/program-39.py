l1=[]
sum=0
n=int(input("Enter the total nuber of element in array"))
print("Enter the elements of array")
for x in range(0,n,1):
    n1=int(input())
    l1.append(n1)
for y in range(0,len(l1),2):
        sum=sum+l1[y]
print("The result is",sum)
