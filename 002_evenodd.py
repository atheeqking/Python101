# This program takes a number as input and the output returns shows if the number is even or odd.

# this statement is to get input from the user
input_num = input("Enter a number:")

# all user inputs are by default strings. This statement is to convert string to integer
input_num = int(input_num)

# this statement checks if the number is divisible by 2
if input_num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
