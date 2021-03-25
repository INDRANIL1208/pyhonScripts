while(True):
    n=int(input("Enter a number"))
    temp=n
    r=0
    while(n>0):
        n1=n%10
        n=n//10
        r=r*10+n1
    print(r)
    n=temp
    if(n==r):
        print("Pallindrome Number")
    else:
        print("Not a Pallindrome Number")
    
