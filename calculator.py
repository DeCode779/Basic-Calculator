program_name = "PyCalc--A Simple Calculator"
version = "1.0"
print(program_name, version)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

operations={
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2 if num2 != 0 else "Error: Division by zero"
}

if operation in operations:
    print(f"{num1}{operation}{num2}={operations[operation]}")
else:
    print("Invalid operation! Please choose from +, -, *, /.")