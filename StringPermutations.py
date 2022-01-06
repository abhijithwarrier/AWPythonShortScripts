# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO FIND THE PERMUTATIONS OF THE USER-INPUT STRING
# USING INBUILT METHOD permutations OF itertools LIBRARY

# Importing necessary module for finding the permutations
from itertools import permutations

# Defining findPermutation() with user-input string as the argument
def findPermutation(inputStr):

    # Finding all the permuatations of the string
    permutationList = permutations(inputStr)

    # Printing each permutations
    print("\nPERMUTATIONS OF THE STRING ARE : \n")
    for item in permutationList:
        print(''.join(item))

# Prompting the user to enter a string
inputSTR = input("\nENTER A STRING : ")

# Calling findPermutation() with user-input string as the argument
findPermutation(inputSTR)
