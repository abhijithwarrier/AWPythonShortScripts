#Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO PRINT FIBONACCI NUMBERS

# Fibonacci numbers are numbers in integer sequence. 0, 1, 1, 2, 3, 5, .... The sequence Fn of
# Fibonacci numbers is defined by recurrence relation Fn=Fn-1+Fn-2 with seed values F0=0 & F1=1.

# Defining FibonacciSeries() function which accepts user-entered number as parameter
def FibonacciSeries(number) :
    # Checking if the number is equals to 0
    if number == 0:
        # If number is equals to 0, then 0 is returned as the output
        print("\nFIBONACCI SERIES : ", str(0))
    # Checking if the number is equals to 1
    if number == 1 :
        # If number is equals to 1, then 1 is returned as the output
        print("\nFIBONACCI SERIES : ", str(1))
    # If number is not equals to 0 or 1, then calculate the fibonacci series
    else :
        # Declaring 2 variables a and b set to 0 and 1 respectively
        a = 0; b = 1
        print("\nFIBONACCI SERIES : ", a, b, end=' ')
        # Executing for loop starting from 2 till the number
        for i in range(2, number):
            # Declaring variable temp which is set to value of b
            temp = b
            # Calculating the sum of a and b and storing it in b
            b = b + a
            # Assigning the value of temp to variable a
            a = temp
            print(b, end=' ')

# Driver Code
if __name__ == '__main__' :
    # Prompting the user to enter a number
    num = int(input("\nENTER THE NUMBER : "))
    # calling the FibonacciSeries() with user input
    FibonacciSeries(num)