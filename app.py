from tkinter import *

# dummy db
names = ['alex', 'robert', 'andy', 'bartholemue', 'jerome', 'lebron', 'davinci', 'jacob', 'the rock', 'spiderman', 'alex', 'robert', 'andy', 'bartholemue', 'jerome', 'lebron', 'davinci', 'jacob', 'the rock', 'spiderman', 'alex', 'robert', 'andy', 'bartholemue', 'jerome', 'lebron', 'davinci', 'jacob', 'the rock', 'spiderman',]

master = Tk()
master.geometry("400x400")

for i in range(len(names)):
    Label(master, text=names[i]).grid(row=i, column=1)



#funny = Label(master, text='(5, 13)').grid(row=5, column=13)

mainloop()