#Prototype Calculator. I need to learn GUI. I'm learning by doing

#I Need to learn clear, and how to use +-*/ instead of if statements

def add(x,y): #add two numbers
	return x+y

def subtract(x,y): #subtract two number
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	return x/y


#Get the numbers, I want to change this to a Switch satement, as well as do this in the proper caculator order
num1 = float(input("Enter the first number: "))
num2 = float(input ("Enter the second number: "))

choice = input ("Do you want to add? subtract? multiply? divide? : ")

if choice == 'add':
	print(num1, "+", num2, "=", add(num1, num2))
	
elif choice == 'subtract':
	print(num1, "-", num2, "=", subtract(num1, num2))
	
elif choice == 'multiply':
	print(num1, "*", num2, "=", multiply(num1, num2))
	
elif choice == 'divide':
	print(num1, "/", num2, "=", divide(num1, num2))
	
elif choice == 'done':
	print("Goodbye")

else:
    print("Not a valid input, please try again")