from tkinter import*
from ttkbootstrap import Style
from tkinter import ttk
import tkinter.font as myfont
def clear():
    global val
    val=""
    entry.set("")
def cal(number):
    global val
    val=val+str(number)
    entry.set(val)

def equal():
   global val
   result=str(eval(val))
   entry.set(result)
    

style=Style()
root=style.master
root.title("calculator")
val=""
entry=StringVar()
entry1=ttk.Entry(root,font=("arial",30),width=27,textvariable=entry)
entry1.grid(row=0,column=0,columnspan=4)
style.configure('primary.TButton',font=("arial",20,"bold"),border=4)
style.configure('warning.TButton',font=("arial",20,"bold"),border=4)
style.configure('danger.TButton',font=("arial",20,"bold"),border=4)

root.config(bg="black")
root.resizable(False,False)
row0=ttk.Button(text="7",command=lambda:cal(7),style="primary.TButton")
row0.grid(row=1,column=0,sticky=W,ipadx=63)
row0=ttk.Button(text="8",command=lambda:cal(8),style="primary.TButton")
row0.grid(row=1,column=1,ipadx=50)
row0=ttk.Button(text="9",command=lambda:cal(9),style="primary.TButton")
row0.grid(row=1,column=2,ipadx=50)
row0=ttk.Button(text="+",command=lambda:cal('+'),style="warning.TButton")
row0.grid(row=1,column=3,ipadx=59)

row1=ttk.Button(text="4",command=lambda:cal(4),style="primary.TButton")
row1.grid(row=2,column=0,sticky=W,ipadx=62,pady=3,padx=1)
row1=ttk.Button(text="5",command=lambda:cal(5),style="primary.TButton")
row1.grid(row=2,column=1,ipadx=50)
row1=ttk.Button(text="6",command=lambda:cal(6),style="primary.TButton")
row1.grid(row=2,column=2,ipadx=50)
row1=ttk.Button(text="-",command=lambda:cal('-'),style="warning.TButton")
row1.grid(row=2,column=3,ipadx=62)


row2=ttk.Button(text="1",command=lambda:cal(1),style="primary.TButton")
row2.grid(row=3,column=0,sticky=W,ipadx=62,padx=1)
row2=ttk.Button(text="2",command=lambda:cal(2),style="primary.TButton")
row2.grid(row=3,column=1,ipadx=50)
row2=ttk.Button(text="3",command=lambda:cal(3),style="primary.TButton")
row2.grid(row=3,column=2,ipadx=50)
row2=ttk.Button(text="*",command=lambda:cal('*'),style="warning.TButton")
row2.grid(row=3,column=3,ipadx=61)


row3=ttk.Button(text="AC",command=clear,style="danger.TButton")
row3.grid(row=4,column=0,sticky=W,ipadx=50,pady=3,padx=1)
row3=ttk.Button(text="=",command=equal,style="warning.TButton")
row3.grid(row=4,column=1,ipadx=49)
row3=ttk.Button(text="0",command=lambda:cal(0),style="warning.TButton")
row3.grid(row=4,column=2,ipadx=50)
row3=ttk.Button(text="%",command=lambda:cal('%'),style="warning.TButton")
row3.grid(row=4,column=3,ipadx=55)
root.mainloop()

  
        
        
        
       

