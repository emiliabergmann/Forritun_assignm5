# Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.
 
# Make sure that you write up the algorithm before starting to code.
# Then implement the algorithm in Python. Put your algorithmic description as a comment in the program file.

#1. Start by getting an input from the user.
#2. Create a constant that holds the highes number, starting at 0.
#3. Use a while loop to repeatly ask the user for a number until he enters a negative value.
#4. Max_int will store the largest number inputted
#5. Everytime a user inputs a number greater then the previous max_int, a new highest number will be set to the max_int
#6. When a negative value is entered, the program will print out the largest number that the user has entered.


num_int = int(input("Input a number: "))    # Do not change this line

max_int = 0
# Fill in the missing code
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)    # Do not change this line  # Do not change this line

