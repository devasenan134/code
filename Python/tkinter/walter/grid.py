from tkinter import *

root = Tk()

# creating a label widget
mylabel1 = Label(root, text="Hello world")
mylabel2 = Label(root, text="my name is devasenan")


# showing it onto the screen
# grid is relative
mylabel1.grid(row = 0, column = 0)
mylabel2.grid(row = 1, column = 1)



root.mainloop()