import tkinter as tk
from tkinter import *
from PIL import Image,ImageDraw

# # win=tk.Tk()

# # image=tk.PhotoImage(file=r"C:\Users\user\Downloads\taskpy\rainbow.png")
# # image=image.
# # lb1=tk.Label(image = image).pack()

# # win.mainloop()

# win=tk.Tk()
# win.title("Information")
# win.geometry("300x300")

# def show_password():
#     pass_str=password.get()
#     passw.config(text = pass_str)


# login=tk.Label(text="Login: ").grid(row=0,column=0)

# lgn=tk.Entry().grid(row=0,column=1)

# password=tk.Label(text="Password: ").grid(row=1,column=0)
# passw=tk.Entry(show="*").grid(row=1,column=1)


# btn1= tk.Button(text="show password",command=show_password)
# # passw=tk.Entry().grid(row=2,column=1)
# rem=tk.Checkbutton(text="Remember").grid(row=3,column=1)


# win.mainloop()

# def edit():
#     global enrty2
#     global btn_save
#     enrty2.pack()
#     btn_save.pack()

#     enrty2.delete("1.0","end-1c")
#     text = entry1['text']
#     print(text)
#     enrty2.insert("1.0",text)  

# def save():
#     global btn_save
#     text=enrty2.get("1.0","end-1c")
#     entry1.config(text=text)
    
#     enrty2.forget()
#     btn_save.forget()

# win=tk.Tk()
# win.title("Info")
# win.geometry("300x300")

# entry1=Label(win,text="Text1")
# entry1.pack()
# Button(win,text='Edit',command=edit).pack()

# enrty2=Text(win)
# btn_save=Button(win,text="Save",command=save)

# win.mainloop()


# def update(value):
#  label.config(font=("Italic",value))

# label = tk.Label(text="NiHao")
# label.pack()

# scale=tk.Scale(win,from_=0,to=100,orient=tk.VERTICAL)
# scale.pack()

# scale1=tk.Scale(win,from_=0,to=100,orient=tk.HORIZONTAL,command=update,resolution=10)
# scale1.pack()

# win.mainloop()

# win=tk.Tk()
# win.geometry("300x300")
# menu=tk.Menu(win)
# menu.add_command(label="File")
# menu.add_command(label="Exit",command=win.destroy)
# win.config(menu=menu)

# submenu=tk.Menu(menu)
# menu.add_cascade(label="Submenu",menu=submenu)
# submenu.add_command(label="Sub1")
# submenu.add_separator()
# submenu.add_command(label="Sub2")
# submenu.add_separator()
# submenu.add_command(label="Sub3")
# submenu.add_separator()


# frame1=tk.Frame(win)
# frame1.pack(side=tk.LEFT)

# lb1 = tk.Label(frame1,text="Sub1")
# lb1.pack()

# frame2 = tk.Frame(win)
# frame2.pack(side=tk.RIGHT)

# lb2=tk.Label(frame1,text="Sub2")
# lb2.pack()


# win.mainloop()



