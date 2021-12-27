# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO SORT USER-INPUT STRING IN ALPHABETICAL ORDER

# The elements stored in a List can be sorted using the sort() method.
# Setting argument reverse=True in sort() sorts the list in descending order

# Defining AlphabeticSort() with user-input string as the argument
def AlphabeticalSort(inputStr):
    # Splitting the string into a list of words and storing them in lower case
    list_of_words = [w.lower() for w in inputStr.split()]
    # Sorting the list using the sort method of the list in Python
    list_of_words.sort()
    # Printing the sorted words
    print("\nTHE SORTED WORDS ARE : ")
    for w in list_of_words:
        print(w)

# Driver Code
if __name__ == '__main__':
    # Prompting the user to enter the string
    inputString = input("\nENTER THE WORDS TO SORT : ")
    # Calling the AlphabeticalSort() function with the user-entered string as parameter
    AlphabeticalSort(inputString)