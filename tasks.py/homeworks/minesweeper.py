# import tkinter as tk
# from tkinter import ttk
# from random import randint

# class MyButton(tk.Button):
#     def __init__(self,master=None,cnf={}, is_bomb:bool= False,x=0,y=0,*args,**kwargs):
#         self.x=x
#         self.y=y
#         self.is_bomb=is_bomb
#         self.around_mines=0
#         super().__init__(master,cnf,**kwargs)

#     def __repr__(self):
#         return f"{self.is_bomb}{self.x}{self.y}"
    
# COL=5
# ROW=5
# BOMBS=10

# win=tk.Tk()
# win.title('Minesweeper')

# def click(btn):
#     if btn.is_bomb:
#         btn.config(text="^_^")
#         show_all()
#     else:
#         btn.config(text=btn.around_mines)

#         btn.config(text=f"{btn.around_mines}")
#     btn.config(state="disabled")

# def show_all():
#     for row in buttons:
#         for b in row:
#             if b.is_bomb:
#                 b.config(text="^_^")
#             else:
#                 b.config(text=f"{b.around_mines}")
#             b.grid(column = b.x,row = b.y)
#             b.config(state="disabled")



# buttons=[]
# for i in range(COL):
#     temp=[]
#     for e in range(ROW):
#         btn=(MyButton(text="*",width=10,x=i,y=e))
#         temp.append(btn)
#     buttons.append(temp)


# def fill_cells():
#     for x in range(COL):
#         for y in range(ROW):
#             if buttons[x][y].is_bomb == False:
#                 mines=0
#                 for i in [-1,0,1]:
#                     for j in [-1,0,1]:
#                         if 0 <= x + i < COL and 0 <= y+j<ROW:
#                             if buttons[x + i][y+j].is_bomb == True:
#                                 mines+=1
#                 buttons[x][y].around_mines = mines

# bomb=BOMBS

# while bomb !=0:
#     rand_col=randint(0,COL-1)
#     rand_row=randint(0,ROW-1)
#     if buttons[rand_row][rand_col].is_bomb:
#         continue
#     bomb -= 1
#     buttons[rand_row][rand_col].is_bomb=True

# fill_cells()

# print(*buttons)
# col=1
# row=2

# for b in buttons:
#     for b in b:
#         print(b,end="\t | ")
#     print()

# for l in buttons:
#     for button in l:
#         button.config(command=lambda btn=button: click(btn))
#         button.grid(column = button.x,row = button.y)


# win.mainloop()

import tkinter as tk
from tkinter import ttk
from random import randint

class MyButton(tk.Button):
    def __init__(self,master=None, cnf = {}, is_bomb:bool=False,x=0,y=0,*args,**kwargs):
        self.x=x
        self.y=y
        self.is_bomb=is_bomb
        self.around_mines=0
        super().__init__(master,cnf,**kwargs)

    def __repr__(self):
        return f"{self.is_bomb}{self.x}{self.y}"
    
COL = 5
ROW = 5
BOMBS = 10

win=tk.Tk()
win.title("Minesweeper")

def click(btn):
    if btn.is_bomb:
        btn.config(text="💣")
    else:
        btn.config(text=f"{btn.around_mines}")
    btn.config(state="disable")

def show_all():
    for row in buttons:
        for b in row:
            b.config(text="💣")
        else:
            b.config(text=f"{b.around_mines}")
        b.grid(column=b.x,row=b.y)
        b.config(state="disable")

buttons=[]
for i in range(COL):
    temp=[]
    for e in range(ROW):
        btn=(MyButton(text="*",width=10,x=i,y=e))
        temp.append(btn)
    buttons.append(temp)

def fill_cells():
    for x in range(COL):
        for y in range(ROW):
            if buttons[x][y].is_bomb == False:
                mines=0
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if 0 <= x+i< COL and 0 <= y + j < ROW:
                         if 0 <= buttons[x + i][y + j].is_bomb==True:
                             mines+=1
                buttons[x][y].around_mines = mines

bomb=BOMBS
while bomb != 0:
    rand_col=randint(0,COL-1)
    rand_row=randint(0,ROW-1)
    if buttons[rand_row][rand_col].is_bomb:
        continue
    bomb-=1
    buttons[rand_row][rand_col].is_bomb=True

fill_cells()
# show_all()

print(*buttons)
col=1
row=2

for b in buttons:
    for b in b:
        print(b,end="\t | ")
    print()

for l in buttons:
    for button in l:
        button.config(command = lambda btn=button: click(btn))
        button.grid(column=button.x,row=button.y)

win.mainloop()
                