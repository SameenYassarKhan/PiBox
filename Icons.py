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

#Defining the button #This still doesn't work
def openCalculator():
 	os.system('python CalculatorV2.py')
 	
#Add the ability to open up the drawing app too
def openDrawing():
	os.system('python DrawingPython.py')

frame = LabelFrame(root, padx = 5, pady = 5)
frame.pack(padx=10,pady=10)

#This line finds an image
Calc_img = ImageTk.PhotoImage(Image.open("Iconleak-Atrous-Calculator.ico"))

Draw_img = ImageTk.PhotoImage(Image.open("drawing.ico"))


	
IconC = Button(frame, text = "Calculator", image = Calc_img, compound="top", command = openCalculator)

IconD = Button(frame, text = 'Drawing', image = Draw_img, compound = "top", command = openDrawing)



IconC.pack()
IconD.pack()

root.mainloop()
