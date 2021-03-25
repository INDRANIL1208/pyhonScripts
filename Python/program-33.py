while(True):
    n=int(input("Enter a Number"))
    temp=n
    s=0
    while(n>0):
        n1=n%10
        n=n//10
        m=1
        for x in range (1,n1+1,1):
            m=m*x
        s=s+m
        if(n>0):
            print(n1,end="!+")
        else:
            print(n1,end="!=")
    print(s)
    n=temp
    if(n==s):
        print("Krishnamurty Number")
    else:
        print("Not a Krishnamurty Number")