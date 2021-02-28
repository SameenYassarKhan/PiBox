#Calculator UI Prototype

from tkinter import *

root = Tk()
root.title("Pi Calculator")

#This is not additon. This just makes the button do things

#Defining what the buttons do. 
def button_click(n):
   e.insert(END, n)

def button_clear():
	e.delete(0, END)

def button_equal(equation):
	answer = eval(equation)
	e.delete(0,END)
	e.insert (0, answer)



#Subtraction
#Multiplication
#Division
#Changing the function from positive to negative
#Clear
#Clear all (do I actually need this?)

#The Buttons
e = Entry(root) #A widget that enters things
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
CalculatorButtonClear = Button (root, text = "C", padx = 10, pady = 10, command = button_clear)
CalculatorButtonNegative = Button (root, text = "-N", padx = 10, pady = 10, command = lambda: button_click("-"))
CalculatorButtonDivide = Button (root, text = "/", padx = 10, pady = 10, command =lambda: button_click("/"))
CalculatorButtonOne = Button (root, text = "1", padx = 10, pady = 10, command = lambda: button_click(1))
CalculatorButton2 = Button (root, text = "2", padx = 10, pady = 10, command = lambda: button_click(2))
CalculatorButton3 = Button (root, text = "3", padx = 10, pady = 10, command = lambda: button_click(3))
CalculatorButtonMultiply = Button (root, text = "*", padx = 10, pady = 10, command =lambda: button_click("*"))
CalculatorButton4 = Button (root, text = "4", padx = 10, pady = 10, command = lambda: button_click(4))
CalculatorButton5 = Button (root, text = "5", padx = 10, pady = 10, command = lambda: button_click(5))
CalculatorButton6 = Button (root, text = "6", padx = 10, pady = 10, command = lambda: button_click(6))
CalculatorButtonMinus = Button (root, text = "-", padx = 10, pady = 10, command =lambda: button_click("-"))
CalculatorButton7 = Button (root, text = "7", padx = 10, pady = 10, command = lambda: button_click(7))
CalculatorButton8 = Button (root, text = "8", padx = 10, pady = 10, command = lambda: button_click(8))
CalculatorButton9 = Button (root, text = "9", padx = 10, pady = 10, command = lambda: button_click(9))
CalculatorButtonAdd = Button (root, text = "+", padx = 10, pady = 10, command = lambda: button_click("+"))
CalculatorButton0 = Button (root, text = "0", padx = 10, pady = 10, command = lambda: button_click(0))
CalculatorButtonDecimal = Button (root, text = ".", padx = 10, pady = 10, command = lambda: button_click("."))
CalculatorButtonEquals = Button (root, text = "=", padx = 10, pady = 10, command = lambda: button_equal(e.get() ) )

# Parentsies. I don't know where to put them yet
CalculatorButtonPar1 = Button (root, text = "(", padx = 10, pady = 10, command = lambda: button_click( "(" ) )
CalculatorButtonPar2 = Button (root, text = ")", padx = 10, pady = 10, command =lambda: button_click( ")" ) )


#To Place Them

#Math.grid(row = 0, column = 1)
CalculatorButtonClear.grid(row = 1, column = 0)
CalculatorButtonPar1.grid(row = 1, column = 1)
CalculatorButtonPar2.grid(row = 1, column = 2)
CalculatorButtonDivide.grid(row = 1, column = 3)
CalculatorButton7.grid(row = 2, column = 0)
CalculatorButton8.grid(row = 2, column = 1)
CalculatorButton9.grid(row = 2, column = 2)
CalculatorButtonMultiply.grid(row = 2, column = 3)
CalculatorButton4.grid(row = 3, column = 0)
CalculatorButton5.grid(row = 3, column = 1)
CalculatorButton6.grid(row = 3, column = 2)
CalculatorButtonMinus.grid(row = 3, column = 3)
CalculatorButtonOne.grid(row = 4, column = 0)
CalculatorButton2.grid(row = 4, column = 1)
CalculatorButton3.grid(row = 4, column = 2)
CalculatorButtonAdd.grid(row = 4, column = 3)
CalculatorButton0.grid(row = 5, column = 0)
CalculatorButtonDecimal.grid(row = 5, column = 1)
CalculatorButtonNegative.grid(row = 5, column = 2)
CalculatorButtonEquals.grid(row = 5, column = 3)



root.mainloop()
