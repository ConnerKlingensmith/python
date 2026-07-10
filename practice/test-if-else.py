number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 >= number2 and number1 >= number3:
    print("Number 1 is the larget number of the three")

elif number2 >= number1 and number2 >= number3:
    print("Number 2 is the larget number of the three")

else:
    print("Number 3 is the larget number of the three")
