# import tkinter as tk
# from tkinter import ttk
# #  TASK1
# # win=tk.Tk()
# # def change():
# #     Label.config(text="Hello,User")
  
# # win.title("Tkinter.com")     
# # win.geometry("300x250") 
# # # def dest():
# # #     print(win.destroy())
# # btn = ttk.Button(text="Click",command = change)
# # btn.pack()  
 
# # Label=ttk.Label(win,text="")
# # Label.pack()

# # win.mainloop()

# # TASK2
# # win=tk.Tk()

  
# # win.title("Tkinter.com")     
# # win.geometry("300x250") 

# # def remove():
# #     entry.delete(0,"end")

# # def back(event):
# #     text = entry.get()
# #     lable.config(text="Hi,User\n"+ text)

# # btn = ttk.Button(text="Delete",command = remove)
# # btn.pack() 

# # entry = ttk.Entry() 
# # entry.pack()
# # entry.bind('<Return>',back)
# # entry.pack()

# # lable=ttk.Label(text="")
# # lable.pack()
# # win.mainloop()

# task CALCULATOR
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
calcul=tk.Tk()
calcul.title("CALCULATOR")
calcul.geometry("300x300+100+100") 
photo=tk.PhotoImage(file="calcu.png")
calcul.iconphoto(False,photo)
calcul['bg']="#33ffe6"
calcu=ttk.Entry()
calcu.grid(row=0,column=0,columnspan=5)

def calculate():
    value=calcu.get()
    calcu.delete(0,"end")
    second_value=""
    if value[-1] in ["+","-","/","*"]:
        second_value = value.split(value[-1])[0]

    try:
        calcu.insert(0,eval(value + second_value))
    except ZeroDivisionError:
        calcu.insert(1,"Нельзя делить на ноль")

def delete():
    calcu.delete(0,"end")
    calcu.insert(0,"0")

def add_operation(operation):
    value = calcu.get()
    if "+" in value or "-" in value or "/" in value or "*" in value:
        value = str(eval(value))

    if value[-1] in ["+","-","/","*"]:
        value = value[:-1]
    calcu.delete(0,"end")
    calcu.insert(0,value + operation)

def add_digit(digit):
    if calcu.get()[0].isalpha():
        calcu.delete(0,"end")
        calcu.insert(0,"0")

    value = calcu.get()
    print(value[0].isalpha())
    if value[0].isalpha():
        calcu.delete(0,"end")

    if value[0] == "0":
        value = value[1:]
    calcu.delete(0,"end")
    calcu.insert(0,value + str(digit))

calcu = tk.Entry(calcu,justify="right",font=("Arial",15), width=15)
calcu.insert(0,"0")
calcu.grid(row=0,column=1,columnspan=4,sticky="we")

ttk.Button(text="1", command=lambda: add_digit(1)).grid(row=1, column=1, sticky="wens")
ttk.Button(text="2", command=lambda: add_digit(2)).grid(row=1, column=2, sticky="wens")
ttk.Button(text="3", command=lambda: add_digit(3)).grid(row=1, column=3, sticky="wens")
ttk.Button(text="4", command=lambda: add_digit(4)).grid(row=2, column=1, sticky="wens")
ttk.Button(text="5", command=lambda: add_digit(5)).grid(row=2, column=2, sticky="wens")
ttk.Button(text="6", command=lambda: add_digit(6)).grid(row=2, column=3, sticky="wens")
ttk.Button(text="7", command=lambda: add_digit(7)).grid(row=3, column=1, sticky="wens")
ttk.Button(text="8", command=lambda: add_digit(8)).grid(row=3, column=2, sticky="wens")
ttk.Button(text="9", command=lambda: add_digit(9)).grid(row=3, column=3, sticky="wens")
ttk.Button(text="0", command=lambda: add_digit(0)).grid(row=4, column=2, sticky="wens")

ttk.Button(text="AC", command=delete).grid(row=4, column=1,sticky="wens")
ttk.Button(text="=", command=calculate).grid(row=4, column=3,sticky="wens")
ttk.Button(text="-", command=lambda: add_operation("-")).grid(row=1, column=4,sticky="wens")
ttk.Button(text="*", command=lambda:add_operation("*")).grid(row=2, column=4,sticky="wens")
ttk.Button(text="/", command=lambda:add_operation("/")).grid(row=3, column=4,sticky="wens")
ttk.Button(text="+", command=lambda:add_operation("+")).grid(row=4, column=4,sticky="wens")

calcu.mainloop()
