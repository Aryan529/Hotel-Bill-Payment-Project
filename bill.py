from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title('Hotel Management System')

text_Input= StringVar()
operator = ''

Tops = Frame(root,width=1600,height=50, bg='powder blue',relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops,font=('Times New Roman',50,'bold'),text="Hotel Management System",fg='steel blue',bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops,font=('arial',20),text=localtime,fg='steel blue',bd=10,anchor='w')
lblinfo.grid(row=1,column=0)


def btnClick(numbers):
    global operator
    operator =  operator + str(numbers)
    text_Input.set( operator)

def btnClearDisplay():
    global operator
    operator=''
    text_Input.set('')

def btnEqual():
    global operator
    sum= str(eval(operator))
    text_Input.set(sum)
    operator = ''

def Ref():
    x=random.randint(10908,500876)
    randomRef= str(x)
    rand.set(randomRef)

def Exit():
    root.destroy()

def Reset():
    rand.set('')
    rand .set('')
    fries.set('')
    drinks .set('')
    tax.set('')
    burger.set('')
    pizza.set('')
    service.set('')
    cake.set('')
    total.set('')
    cost.set('')
    subtotal.set('')



txtDisplay = Entry(f2,font=('Times New Roman',20,'bold'),textvariable=text_Input,
                   bd=10,insertwidth=2,bg='powder blue',justify='right')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='7',bg='green',command= lambda: btnClick(7)).grid(row=2,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='8',bg='green',command= lambda: btnClick(8)).grid(row=2,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='9',bg='green',command= lambda: btnClick(9)).grid(row=2,column=2)

Addition= Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='+',bg='green',command= lambda: btnClick('+')).grid(row=2,column=3)
#--------------------------------------------------------------------------------------------------
btn4 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='4',bg='green',command= lambda: btnClick(4)).grid(row=3,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='5',bg='green',command= lambda: btnClick(5)).grid(row=3,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='6',bg='green',command= lambda: btnClick(6)).grid(row=3,column=2)

Subtraction= Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='-',bg='green',command= lambda: btnClick('-')).grid(row=3,column=3)
#--------------------------------------------------------------------------------------------------
btn1 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='1',bg='green',command= lambda: btnClick(1)).grid(row=4,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='2',bg='green',command= lambda: btnClick(2)).grid(row=4,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='3',bg='green',command= lambda: btnClick(3)).grid(row=4,column=2)

Multiply = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='x',bg='green',command= lambda: btnClick('x')).grid(row=4,column=3)
#--------------------------------------------------------------------------------------------------
btn0 = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='0',bg='green',command= lambda: btnClick(0)).grid(row=5,column=0)

btnClear = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='C',bg='green',command=btnClearDisplay).grid(row=5,column=1)

btnEqual = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='=',bg='green',command=btnEqual).grid(row=5,column=2)

Divide = Button(f2,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),
              text='/',bg='green',command= lambda: btnClick('/')).grid(row=5,column=3)

#------------------------------Reference 1------------------------------------------------------------------

rand = StringVar()
fries = StringVar()
drinks = StringVar()
tax = StringVar()
burger = StringVar()
pizza = StringVar()
service = StringVar()
cake = StringVar()
total = StringVar()
cost = StringVar()
subtotal = StringVar()



lblReference = Label(f1,font=('Times New Roman',16,'bold'),text='Reference',
                     bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=rand,
                     bd=16,insertwidth=4,bg='powder blue',justify='right')
txtReference.grid(row=0,column=1)
#------------------------------------------------------------------------------------
lblfries = Label(f1,font=('Times New Roman',16,'bold'),text='Fries',
                     bd=16,anchor='w')
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=fries,
                     bd=16,insertwidth=4,bg='powder blue',justify='right')
txtfries.grid(row=1,column=1)
#------------------------------------------------------------------------------------
lbldrinks = Label(f1,font=('Times New Roman',16,'bold'),text='Drinks',
                     bd=16,anchor='w')
lbldrinks.grid(row=2,column=0)
txtdrinks = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=drinks,
                     bd=16,insertwidth=4,bg='powder blue',justify='right')
txtdrinks.grid(row=2,column=1)
#------------------------------------------------------------------------------------
lblburger = Label(f1,font=('Times New Roman',16,'bold'),text='Veg Burger',
                     bd=16,anchor='w')
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=burger,
                     bd=16,insertwidth=4,bg='powder blue',justify='right')
txtburger.grid(row=3,column=1)
#------------------------------------------------------------------------------------
lblpizza = Label(f1,font=('Times New Roman',16,'bold'),text='Veg Pizza',
                     bd=16,anchor='w')
lblpizza.grid(row=4,column=0)
txtpizza = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=pizza,
                     bd=16,insertwidth=4,bg='powder blue',justify='right')
txtpizza.grid(row=4,column=1)
#------------------------------------------------------------------------------------
lblcake = Label(f1,font=('Times New Roman',16,'bold'),text='Lava Cake',
                     bd=16,anchor='w')
lblcake.grid(row=5,column=0)
txtcake = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=cake,
                     bd=16,insertwidth=4,bg='powder blue',justify='right')
txtcake.grid(row=5,column=1)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Reference 2 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4

lblcost = Label(f1,font=('Times New Roman',16,'bold'),text='Cost',
                     bd=16,anchor='w')
lblcost.grid(row=0,column=2)
txtcost = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=cost,
                     bd=16,insertwidth=4,bg='powder blue',justify='right')
txtcost.grid(row=0,column=3)
#------------------------------------------------------------------------------------
lblservice = Label(f1,font=('Times New Roman',16,'bold'),text='Service Charge',
                     bd=16,anchor='w')
lblservice.grid(row=1,column=2)
txtservice = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=service,
                     bd=16,insertwidth=4,bg='powder blue',justify='right')
txtservice.grid(row=1,column=3)
#------------------------------------------------------------------------------------
lbltax = Label(f1,font=('Times New Roman',16,'bold'),text='TAX',
                     bd=16,anchor='w')
lbltax.grid(row=2,column=2)
txttax = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=tax,
                     bd=16,insertwidth=4,bg='powder blue',justify='right')
txttax.grid(row=2,column=3)
#------------------------------------------------------------------------------------
lblsubtotal = Label(f1,font=('Times New Roman',16,'bold'),text='Sub Total',
                     bd=16,anchor='w')
lblsubtotal.grid(row=3,column=2)
txtsubtotal = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=subtotal,
                     bd=16,insertwidth=4,bg='powder blue',justify='right')
txtsubtotal.grid(row=3,column=3)
#------------------------------------------------------------------------------------
lbltotal = Label(f1,font=('Times New Roman',16,'bold'),text='Total Cost',
                     bd=16,anchor='w')
lbltotal.grid(row=4,column=2)
txttotal = Entry(f1,font=('Times New Roman',16,'bold'),textvariable=total,
                     bd=16,insertwidth=4,bg='yellow',justify='right')
txttotal.grid(row=4,column=3)



btntotal = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('Times New Roman',16,'bold'),
                  width=10,text='Total',bg='powder blue',command=Ref).grid(row=7,column=1)
btnReset = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('Times New Roman',16,'bold'),
                  width=10,text='RESET',bg='powder blue',command=Reset).grid(row=7,column=2)
btnExit = Button(f1,padx=16,pady=8,bd=16,fg='black',font=('Times New Roman',16,'bold'),
                  width=10,text='EXIT',bg='powder blue',command=Exit).grid(row=7,column=3)






root.mainloop()