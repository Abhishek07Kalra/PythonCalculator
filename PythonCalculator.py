from tkinter import *
cal = Tk()
operator=""    
def clear():
    global operator
    operator=""
    text_Input.set("")
def equal():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
def sqrt():
    global operator
    if  (operator==""):
        text_Input.set("ERROR")
    sqrt=int(operator)
    s=sqrt*sqrt
    text_Input.set(s)
    operator=str(s)
def d():
    global operator
    s=int(operator)
    r=int(operator)-(s%10)
    r=r//10
    text_Input.set(str(r))
    operator=str(r)
    
def dx():
       global operator
       r=(1/int(operator))
       text_Input.set(str(r))
       operator=str(r)
def button(number):
    global operator
    operator=operator+str(number)
    text_Input.set(operator)
cal.title("calcultor")
text_Input =StringVar()
txtDisplay = Entry(cal,font=('arial',30,'bold'),textvariable=text_Input,bd=30,
                 insertwidth=4,bg="white",justify="right").grid(columnspan=5)
button7=Button(cal,padx=16,bd=8,text="7",command=lambda:button(7),font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6).grid(row=1,column=0,sticky='w')

button8=Button(cal,padx=16,bd=8,text="8",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button(8)).grid(row=1,column=1,sticky='w')

button9=Button(cal,padx=16,bd=8,text="9",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button(9)).grid(row=1,column=2,sticky='w')
button4=Button(cal,padx=16,bd=8,text="4",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button(4)).grid(row=2,column=0,sticky='w')
button5=Button(cal,padx=16,bd=8,text="5",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button(5)).grid(row=2,column=1,sticky='w')
button6=Button(cal,padx=16,bd=8,text="6",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button(6)).grid(row=2,column=2,sticky='w')
button1=Button(cal,padx=16,bd=8,text="1",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button(1)).grid(row=3,column=0,sticky='w')
button2=Button(cal,padx=16,bd=8,text="2",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button(2)).grid(row=3,column=1,sticky='w')
button3=Button(cal,padx=16,bd=8,text="3",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button(3)).grid(row=3,column=2,sticky='w')
button0=Button(cal,padx=16,bd=8,text="0",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button(0)).grid(row=4,column=0,sticky='w')
buttondx=Button(cal,padx=16,bd=8,text="1/x",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=dx).grid(row=3,column=3,sticky='w')
buttonback=Button(cal,padx=16,bd=8,text="del.",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=d).grid(row=1,column=3,sticky='w')
buttonac=Button(cal,padx=16,bd=8,text="AC",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=clear).grid(row=4,column=1,sticky='w')
buttonequal=Button(cal,padx=16,bd=8,text="=",font=('arial',10,'bold'),fg="black",
               bg="sky blue",height=3,width=6,command=equal).grid(row=4,column=2,sticky='w')

buttonsum=Button(cal,padx=16,bd=8,text="+",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button("+")).grid(row=1,column=4,sticky='w')
buttonsub=Button(cal,padx=16,bd=8,text="-",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button("-")).grid(row=2,column=4,sticky='w')
buttonmul=Button(cal,padx=16,bd=8,text="x",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button("*")).grid(row=3,column=4,sticky='w')
buttondiv=Button(cal,padx=16,bd=8,text="/",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button("/")).grid(row=4,column=4,sticky='w')
sqrt=Button(cal,padx=16,bd=8,text="X2",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=sqrt).grid(row=2,column=3,sticky='w')
point=Button(cal,padx=16,bd=8,text=".",font=('arial',10,'bold'),fg="black",
               bg="grey",height=3,width=6,command=lambda:button(".")).grid(row=4,column=3,sticky='w')
cal.mainloop()
