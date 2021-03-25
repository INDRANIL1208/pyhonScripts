from tkinter import*

def fun_num(n1):
    global k1
    global k2
    global k3
    if(k1==0):
        v1.set(n1)
        k1=1
    else:
        x=str(v1.get())
        v1.set(x+n1)
    k2=0


def fun_opr(n2):
    global k1
    global k2
    global k3
    if(k2==0 and k3==0):
        y=str(v1.get())
        v1.set(y+n2)
        k2=1
        k3=0
    elif(k2==0 and k3==1):
        fun_back()
        y=str(v1.get())
        v1.set(y+n2)
        k2=1
        k3=0
    elif(k2==1 and k3==0):
        y=str(v1.get())
        v1.set(y+n2)
        k1=1
        k2=1
        k3=0


def fun_dot(n3):
    global k3
    global k2
    if(k3==0):
        z=str(v1.get())
        v1.set(z+n3)
        k3=1
        k2=1
    else:
        pass


def fun_equal():
    n4=str(v1.get())
    a1=eval(n4)
    v1.set(a1)
   


def fun_back():
    global k1
    global k2
    global k3
    n5=str(v1.get())
    a3=n5[0:len(n5)-1]
    v1.set(a3)
    ch1=n5[len(n5)-1:len(n5)]
    ch2=n5[len(n5)-2:len(n5)-1]
    if(ch1=='+' or ch1=='-' or ch1=='*' or ch1=='/'):
        k2==0
    elif(ch1=='.'):
        k3=0
    else:
        if(ch2=='+' or ch2=='-' or ch2=='*' or ch2=='/'):
            k2=1
        elif(ch1=='.'):
            k3=1


root=Tk()
root.title("Calculator")
# root.geometry("500x500")

k1=0
k2=0
k3=0


v1=StringVar()
v1.set("0")


Entry(root,bg="powderblue",font=("arial",20,"bold"),bd="20",textvariable=v1,justify="right").grid(columnspan=4)
Button(root,padx=16,text="1",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_num('1')).grid(row=1,column=0)
Button(root,padx=16,text="2",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_num('2')).grid(row=1,column=1)
Button(root,padx=16,text="3",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_num('3')).grid(row=1,column=2)
Button(root,padx=16,text="+",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_opr('+')).grid(row=1,column=3)


Button(root,padx=16,text="4",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_num('4')).grid(row=2,column=0)
Button(root,padx=16,text="5",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_num('5')).grid(row=2,column=1)
Button(root,padx=16,text="6",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_num('6')).grid(row=2,column=2)
Button(root,padx=16,text="-",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_opr('-')).grid(row=2,column=3)


Button(root,padx=16,text="7",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_num('7')).grid(row=3,column=0)
Button(root,padx=16,text="8",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_num('8')).grid(row=3,column=1)
Button(root,padx=16,text="9",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_num('9')).grid(row=3,column=2)
Button(root,padx=16,text="*",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_opr('*')).grid(row=3,column=3)


Button(root,padx=16,text=".",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_dot('.')).grid(row=4,column=0)
Button(root,padx=16,text="0",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_num('0')).grid(row=4,column=1)
Button(root,padx=16,text="=",bg="grey",font=("arial",20,"bold"),bd="20",command=fun_equal).grid(row=4,column=2)
Button(root,padx=16,text="/",bg="grey",font=("arial",20,"bold"),bd="20",command=lambda:fun_opr('/')).grid(row=4,column=3)


Button(root,padx=16,text="C",bg="grey",font=("arial",20,"bold"),bd="20",command=fun_back).grid(row=5,column=0)

root.mainloop()