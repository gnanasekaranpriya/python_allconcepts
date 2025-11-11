# Examples 
# Basic if-elif-else structure

#user_input = int(input("Enter any number and the program will tell you if it's positive, negative, or zero: "))

#if user_input == 0: 
#    print("The number is zero.")
#elif user_input > 0:
#    print("The number is positive.")
#else:
#    print("The number is negative.")

# Largest of three numbers

num1 = list(map(int, input("Enter 3 numbers: ").split()))
print(max(num1))

# Menu Driven Calculator 
user_numbers = input("Enter two numbers separated by space: ")
num = list(map(int, user_numbers.split()))
user_choice = input("Enter an operation (+, -, x, /): ")
if user_choice =='+': 
    print(num[0] + num[1])
elif user_choice == '-':
    print(num[0] - num[1])
elif user_choice == 'x':
    print(num[0] * num[1])
elif user_choice == '/':
    print(num[0] / num[1])
else: 
    print("Invalid operation")

    
