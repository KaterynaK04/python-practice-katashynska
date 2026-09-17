print("Kateryna Katashynska, IT-31")

first_number = float(input("Enter the first number (decimal): "))
operation = input("Enter the operation (+, -, *, /, //, %, **): ").strip()
second_number = float(input("Enter the second number (decimal): "))

if operation == "+":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result:.4f}")
elif operation == "-":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result:.4f}")
elif operation == "*":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result:.4f}")
elif operation == "/":
    if second_number == 0:
        print("Error: division by zero is not allowed")
    else:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.4f}")
elif operation == "//":
    if second_number == 0:
        print("Error: division by zero is not allowed")
    else:
        result = first_number // second_number
        print(f"{first_number} // {second_number} = {result:.4f}")
elif operation == "%":
    if second_number == 0:
        print("Error: division by zero is not allowed")
    else:
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result:.4f}")
elif operation == "**":
    result = first_number ** second_number
    print(f"{first_number} ** {second_number} = {result:.4f}")
else:
    print(f"Unknown operation: {operation}")