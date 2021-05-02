from tkinter import *
import time
from datetime import date

root = Tk()

date = date.today()
currentDate = date.strftime('%m-%d-%y')
currentTime = time.strftime('%H:%M %p')

label = Label(root, text = currentTime + '\n' + currentDate, font = ('Helvetica', 12), fg = 'azure', bg = 'gray35')
label.pack(anchor='center')

mainloop()
