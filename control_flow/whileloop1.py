# # Print numbers from 1 to 10 using a while loop.
# i = 1
# while i < 11: 
#     print(i)
#     i = i + 1 

# #Ask the user to enter a number n and print all numbers from 1 to n.
# user_input = int(input("Enter a integer: "))

# j = 1
# while j < user_input: 
#     print(j)
#     j = j + 1 

# #Ask the user to guess a secret number (e.g., 7). 
# #Keep asking until they guess it correctly. Print “Congratulations!” when they do.
# user_guess = int(input("Guess a number: "))
# secret_num = 10
# while user_guess != secret_num: 
#     print("Guess again")
#     user_guess = int(input("Guess a number: "))
# print('Congratulations!')

# # Task 4: Ask the user for a number and keep doubling it until it becomes greater than 1000. 
# # Print the final number.
# value = int(input('Enter a number below 1000: '))

# while value < 1000: 
#     value = value * 2 
# print(value)

#Task 5: Print numbers from 1 to 20, but skip multiples of 3 using continue.
n = 1 
while n < 21:  
    if n % 3 == 0: 
        n += 1 
        continue 
    else: 
        print (n)
    n += 1 

#Task 6: Ask the user to enter numbers continuously.
# Stop when the user enters 0, and then print the sum of all entered numbers.

n = int(input('Enter any number: '))
sum_all = 0

while n != 0: 
    sum_all += n  
    n = int(input('Enter any number: '))
    if n == 0: 
        break
print(sum_all)

