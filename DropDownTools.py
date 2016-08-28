from tkinter import *


def doNothing():
    print("Do Nothing.")


root = Tk()

menu = Menu(root)
root.config(menu=menu) #We're configuring a menu called menu

subMenu = Menu(menu) #A menu that geos in menu.
#cascade params = Name, name of menu object that drops down
menu.add_cascade(label="File", menu=subMenu)
#The following two are both options of the FILE dropdown menu
subMenu.add_command(label="New Project", command=doNothing)
subMenu.add_command(label="New Label", command=doNothing)
subMenu.add_separator() #Just adds seperators between menu things. looks prettier?
subMenu.add_command(label="Exil", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()