# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO PRINT A STATEMENT IN A USER-SPECIFIED FILE USING print() METHOD

# Defining file and its path into which the statements are to be printed
fileName = "YOUR DESTINATION FILE PATH"

# Opening the file in write mode with IN_file as the file object
with open(fileName, 'w') as IN_file:
    # Printing the statements to the file with the argument file set equals to
    # the above file object
    print("THIS IS A TEST FILE.", file=IN_file)
    print("THIS IS A PYTHON PROGRAMMING LANGUAGE EXAMPLE.", file=IN_file)
    print("THIS PROGRAM PRINTS THE PRINT STATEMENT IN A FILE.", file=IN_file)

print("\nALL THE STATEMENTS HAVE BEEN PRINTED INTO THE ABOVE FILE.")
