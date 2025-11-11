# Finding factorial of a number using for loop
value = int(input("input a number for factorial: "))
mul = 1
for i in range(value, 1, -1): 
    mul = mul * i 
print("Factorial of", value, "is", mul)

# While loop 
user_number = int(input("Guess a number: "))
while user_number != 50: 
    print("Please guess the number again!")
    user_number = int(input("Guess a number: "))
else: 
    print("Guessed the correct number!")

# While loop 
# Take a number from the user and sum the all the numbers together 
user_number = input('Enter a number:')
i = 0 
sum = 0 
while i < len(user_number): 
    sum = sum + int(user_number[i])
    i = i + 1 
print(sum)

# Reverse a Number
user_number1 = input('Enter a number:')
i = len(user_number1) - 1

while i < len(user_number1) and i > -1: 
    print(user_number1[i], end = '')
    i = i - 1



