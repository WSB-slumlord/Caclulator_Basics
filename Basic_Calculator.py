def calculator():
    number1=input("Enter the first number of the calculation:")
    operator=input("Enter '-' for subtraction, '+' for addition, '*' for multiplication, '/' for division:")
    number2=input("Enter the second number of the calculation:")

    number1 = float(number1)
    number2 = float(number2)

    if operator =="-":
        print(number1 - number2)
    if operator =="+":
        print(number1 + number2)
    if operator =="*":
        print(number1 * number2)
    if operator =="/":
        print(number1 / number2)

    repeat=input("Would you like to run again? 'yes' or 'no' :")
    if repeat =="yes":
        calculator()

calculator()