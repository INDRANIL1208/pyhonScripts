import tkinter as tk
def fun_add():
    a1=int(v1.get())
    a2=int(v2.get())
    a3=a1+a2
    v3.set(str(a3))

frame=tk.Tk()
frame.title("Calculator")
frame.geometry("500x400")

v1=tk.StringVar()
v2=tk.StringVar()
v3=tk.StringVar()

tk.Label(frame,text="Enter 1st Number",bg="green",fg="yellow",font=("arial",10,"bold")).grid(row=0,column=0)
tk.Entry(frame,text="",textvariable=v1,fg="green",bd="20").grid(row=1,column=0)
tk.Label(frame,text="Enter 2nd Number",bg="green",fg="yellow",font=("arial",10,"bold")).grid(row=2,column=0)
tk.Entry(frame,text="",textvariable=v2,fg="green",bd="20").grid(row=3,column=0)
tk.Button(frame,text="ADD",command=fun_add,bg="green",fg="yellow",font=("arial",12,"bold")).grid(row=4,column=0)
tk.Label(frame,text="Answer",textvariable=v3,fg="green",font=("arial",10,"bold")).grid(row=5,column=0)

frame.mainloop()