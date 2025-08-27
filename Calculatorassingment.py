first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
operation = input("Enter your operation (+, -, *, /, %): ")

if operation == "*":
    print(f"The product is: {first_number * second_number}")
elif operation == "-":
    print(f"The difference is: {first_number - second_number}")
elif operation == "+":
    print(f"The sum is: {first_number + second_number}")
elif operation == "/":
    if second_number == 0:
        print("Error! try other denominator from zero.")
    else:
        print(f"The quotient is: {first_number / second_number}")
elif operation == "%":
    if second_number == 0:
        print("Error! Modulo by zero try other number.")
    else:
        print(f"The remainder is: {first_number % second_number}")
else:
    print("Invalid operation!")
