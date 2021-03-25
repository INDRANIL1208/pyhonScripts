for r in range (0,4,1):
    k=1
    for c in range(0,r+1,1):
        print(k,end='')
        k=k+1
    print("*"*(3-r))