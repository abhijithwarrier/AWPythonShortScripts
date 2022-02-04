# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO CHECK WHETHER THE ENTERED NUMBER IS HARSHAD NUMBER OR NOT

# In Mathematics, a number is called HARSHAD NUMBER, if the number is divisble by
# the sum of the digits present in the number.

# Defining a function called checkHarshadNo() with the number variable as the parameter
def checkHarshadNo(number):
    # Storing the copy of the user-entered number in a new variable called number_copy
    number_copy = number
    # Declaring a new variable called sum_of_digits and setting it to 0
    sum_of_digits = 0
    # Calculating sum of the digits present in the number
    for d in str(number):
        sum_of_digits += int(d)
    # Checking whether the user-entered number is divisible by the sum_of_digits value
    if number % sum_of_digits == 0:
        # printing the result
        print("\n" + str(number) + " IS A HARSHAD NUMBER")
    else:
        # printing the result
        print("\n" + str(number) + " IS NOT A HARSHAD NUMBER")

# Driver Code
if __name__ == '__main__':
    # Prompting the user to enter the number to check and converting it into int type
    num = int(input("ENTER THE NUMBER TO CHECK : "))
    # Calling the checkHarshadNo() function with the user-entered number as parameter
    checkHarshadNo(num)
