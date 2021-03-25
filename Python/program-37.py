def print_menu():
    print("1.To Perform Addition")
    print("2.To print display message")
print_menu()


def f1():
    x=int(input("Enter 1st number"))
    y=int(input('Enter 2nd number'))
    z=x+y
    print(z)
def f2():
    x="hello"
    print(x)
while(True):
    x=int(input("Enter a number to choose"))
    if(x==1):
        f1()
    elif(x==2):
        f2()
        break
    else:
        print("Wrong Input")

