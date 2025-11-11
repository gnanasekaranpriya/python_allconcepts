# Using break -- 
# Question:
# Write a program that keeps asking the user to enter a number.
# If the user enters a negative number, stop the loop immediately using break.
# Otherwise, keep printing “Number accepted”.

while True: 
    user_input = int(input('Enter any number: '))
    if user_input < 0: 
        break 
    else: 
        print("Number accepted")

#Use a for loop to print numbers from 1 to 20,
# but skip all numbers divisible by 3 using continue.
for i in range(0, 20): 
    if i %  3 == 0: 
        continue
    else:
        print(i, end= ' ')
