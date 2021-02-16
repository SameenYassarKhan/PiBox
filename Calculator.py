#Prototype Calculator. I need to learn GUI. I'm learning by doing


#Get the numbers, I want to change this to a Switch satement, as well as do this in the proper caculator order
x = float(input("Enter the first number: "))

choice = input ("Pick one: +, -, *, / : ")

if choice == '+':
        y = float(input("Enter the second number: "))
        print(x, "+", y, "=", x+y)
	
elif choice == '-':
	y = float(input("Enter the second number: "))
	print(x, "-", y, "=", x-y)
	
elif choice == '*':
    y = float(input("Enter the second number: "))
    print(x, "*", y, "=", x*y)
	
elif choice == '/':
	y = float(input("Enter the second number: "))
	print(x, "/", y, "=", x/y)
	
elif choice == 'done':
	print("Goodbye")

else:
    print("Not a valid input, please try again")
