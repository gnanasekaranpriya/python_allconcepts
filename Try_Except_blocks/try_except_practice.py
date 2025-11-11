# Practicing the concept 
# Basically the point is to not show the user the error from command but rather 
# an error that is understandable for the user 

# f = open('testfile.txt') 
# - error from running the command 
# Traceback (most recent call last):
#   File "c:\Users\vgpsa\Python Projects\Data Analyst\Data Collection\Try_Except_blocks\try_except_practice.py", line 5, in
#  <module>
#     f = open('testfile.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'testfile.txt'

# try: 
#     f = open('testfile.txt') 
# except FileNotFoundError as e: 
#     print(e)
# except Exception: 
#     print("Sorry. This file does not exist")
# else: # only runs if there is no exception
#     print(f.read())
#     f.close()
# finally: # runs regardless if there is an exception or there is no exception
#     print("Executing Finally..")

# Practice 2 
try: 
    int(input("Enter a number: "))
except ValueError: # catches that specific value error and not just every error 
    print('This is not a integer')
else: 
    print('This is a number!')
finally: 
    print('code is over!')

# Practice 3 - 

# Asks the user to input two numbers.
# Tries to divide the first number by the second.
# Handles these exceptions specifically:
# ValueError → if the user enters something that is not a number.
# ZeroDivisionError → if the user tries to divide by zero.
# If no exceptions occur, print the result in the format:
# "Result: <result>"
# Always print "Calculation finished" at the end, whether there was an error or not.

try: 
    num1, num2 = input("Give me 2 numbers: ").split()
    div = int(num1)/int(num2)
except ValueError as v: 
    print(v)
except ZeroDivisionError as z: 
    print(z)
else:
    print(div)
finally: 
    print('Calculation is done')

    