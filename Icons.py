#Make icons
#I need a picture with text
#Maybe impliment a double click featue?

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

#PIL is used to allow the use of .pngs. It needs to installed with typeing pip install Pillow in the terminal
root = Tk()
root.title("Main Menu")
#root.iconbitmap("Iconleak-Atrous-Calculator.ico")

#Defining the button #This still doesn't work
def openCalculator():
 	os.system('python CalculatorV2.py')
 	


frame = LabelFrame(root, padx = 5, pady = 5)
frame.pack(padx=10,pady=10)

#This line finds an image
Calc_img = ImageTk.PhotoImage(Image.open("Iconleak-Atrous-Calculator.ico"))
#Calc_img = Calc_img.resize((50,50), Image.ANTIALIAS)
#self.pw.pic = ImageTk.PhotoImage(image)


	
IconC = Button(frame, text = "Calculator", image = Calc_img, compound="top", command = openCalculator)

IconC.pack()

root.mainloop()