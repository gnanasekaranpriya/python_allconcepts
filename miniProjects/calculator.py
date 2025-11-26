#2. Simple Calculator
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the calculation using functions.
# Keep asking until the user wants to exit.

# Optional Challenge:
#Add exception handling for division by zero
# Add more operations like % and **

num1, num2 = map(int, input('Enter 2 integers: ').split())
oper = input('Give me an operation: ')
i = 1

while i != 0: 
    if oper == '+': 
        answer = num1 + num2 
    elif oper == '-': 
        answer = num1 - num2 
    elif  oper == '*': 
        answer = num1 * num2 
    elif  oper == '/': 
        try: 
            answer = num1 / num2 
        except ZeroDivisionError: 
            print("Can't Divide by 0")
    print(answer)
    num1, num2 = map(int, input('Enter 2 integers: ').split())
    oper = input('Give me an operation: ')
    i += 1 


# Code by chat - 
# 2. Simple Calculator
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the calculation using functions.
# Keep asking until the user wants to exit.

while True:
    raw = input("Enter 2 integers separated by space (or type 'exit' to quit): ")
    if raw.strip().lower() == 'exit':
        break
    try:
        num1, num2 = map(int, raw.split())
    except ValueError:
        print("Invalid input. Please enter two integers.")
        continue

    oper = input("Give me an operation (+, -, *, /, %, **). Type 'exit' to quit: ").strip()
    if oper.lower() == 'exit':
        break

    if oper == '+':
        answer = num1 + num2
    elif oper == '-':
        answer = num1 - num2
    elif oper == '*':
        answer = num1 * num2
    elif oper == '/':
        try:
            answer = num1 / num2
        except ZeroDivisionError:
            print("Can't divide by zero.")
            continue
    elif oper == '%':
        try:
            answer = num1 % num2
        except ZeroDivisionError:
            print("Can't modulo by zero.")
            continue
    elif oper == '**':
        answer = num1 ** num2
    else:
        print("Unknown operation.")
        continue

    print("Answer:", answer)
