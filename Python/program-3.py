def func1(list1):
    if (list1[-1]==list[0] and list1[0]%2==0):
        print("condition is satisfied")
    else:
        print("Condition is not satisfied")
    return func1
    #driver code
if __name__=="__main__":
        list1=[]
        n= int(input("Enter the limit of the array"))
        for i in range(0,n,1):
            element=int(input("Enter the elements of the array"))
            list1.append(element)
    func1(list1)
