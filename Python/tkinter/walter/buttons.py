from tkinter import *

root = Tk()

def myclick():
	mylabel = Label(root, text="Look I clicked a button!")
	mylabel.pack()

mybutton = Button(
	root,
	text="Click here!",
	padx=50,
	pady=10,
	command=myclick,
	fg = 'red',
	bg = 'black'
	)

mybutton.pack()

root.mainloop()