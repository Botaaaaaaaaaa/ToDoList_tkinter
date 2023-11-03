import tkinter as tk
from tkinter import ttk

def del_info():
    window.delete(0,"end")
    window.insert(0,"0")

window = tk.Tk()
window.title("Введите домашний адрес")


lbl_first_name = tk.Label(text="Имя:")
ent_first_name = tk.Entry( width=50)
lbl_first_name.grid(row=0, column=0, sticky="e")
ent_first_name.grid(row=0, column=1)

lbl_last_name = tk.Label( text="Фамилия:")
ent_last_name = tk.Entry(width=50)
lbl_last_name.grid(row=1, column=0, sticky="e")
ent_last_name.grid(row=1, column=1)
 

lbl_address1 = tk.Label(text="Адрес :")
ent_address1 = tk.Entry( width=50)

lbl_address1.grid(row=2, column=0, sticky="e")
ent_address1.grid(row=2, column=1)
 
lbl_city = tk.Label( text="Город:")
ent_city = tk.Entry( width=50)

lbl_city.grid(row=4, column=0, sticky="e")
ent_city.grid(row=4, column=1)

lbl_state = tk.Label(text="Регион:")
ent_state = tk.Entry( width=50)

lbl_state.grid(row=5, column=0, sticky="e")
ent_state.grid(row=5, column=1)

lbl_postal_code = tk.Label( text="Почтовый индекс:")
ent_postal_code = tk.Entry(width=50)
lbl_postal_code.grid(row=6, column=0, sticky="e")
ent_postal_code.grid(row=6, column=1)
 
lbl_country = tk.Label(text="Страна:")
ent_country = tk.Entry( width=50)

lbl_country.grid(row=7, column=0, sticky="e")
ent_country.grid(row=7, column=1)

btn_submit = tk.Button(text="Отправить").grid(row=8,column=1, padx=10)

btn_clear = tk.Button(text="Очистить",command=del_info).grid(row=8,column=1,padx=10)
 
window.mainloop()