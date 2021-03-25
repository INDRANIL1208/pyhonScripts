n=int(input("Enter a number"))
y=len(str(n))
temp=n
s=0
while(n>0):
    n1=n%10
    n=n//10
    s=s+n1**y
    if(n>0):
        print(n1**y,end='+')
    else:
        print(n1**y,end='=')
print(s)
n=temp
if(n==s):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
