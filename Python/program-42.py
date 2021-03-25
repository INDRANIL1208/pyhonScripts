"""def mymain():
    print("My name is Dash")
def summy(firstOperand=1,secondOperand=2):
    return firstOperand+secondOperand

if __name__=="__main__":
 print( summy(123,56))"""


def dup_num(list1):
    rep=[]
    len_list1=len(list1)
    for i in range(0,len_list1,1):
        k=i+1
        for j in range(k,len_list1,1):
            if(list1[i]==list1[j]) and list1[i] not in rep:
                rep.append(list1[i])
    print(rep)
    return rep

#driver code
if __name__=="__main__":
 list1=[]
 n=int(input("Enter the limit of the array"))
 for i in range (0,n,1):
    list1_element=int(input("Enter the elements of the array"))
    list1.append(list1_element)
 print(list1)    
 dup_num(list1)