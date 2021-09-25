# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO CHECK WHETHER THE USER-ENTERED WORDS ARE ANAGRAMS OR NOT

# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Defining the checkAnagram() function with str1 and str2 as the arguments to check the string
def checkAnagram(str1, str2):
    # Finding the lengths of the 2 strings
    str1_length = len(str1)
    str2_length = len(str2)
    # If the 2 lengths are not equal, the given strings are not anagrams
    if str1_length != str2_length:
        # Printing the result
        print("\n", str1, " AND ", str2, " ARE NOT ANAGRAMS.")

    # Sorting the strings using in-built sorted() method that returns the list of characters
    str1_sorted_list = sorted(str1)
    str2_sorted_list = sorted(str2)

    # Compare the elements of sorted lists. If they are same, the given strings are anagrams
    if str1_sorted_list == str2_sorted_list:
        print("\n" + str1 + " AND " + str2 + " ARE ANAGRAMS.")
    else:
        print("\n" + str1 + " AND " + str2 + " ARE NOT ANAGRAMS.")

# Driver code
if __name__ == '__main__':
    # Prompting the user to enter the words to check
    string1, string2 = input("ENTER THE WORDS TO CHECK SEPARATED BY COMMA : ").split(',')
    # Calling the checkAnagran() function with the user-entered strings as parameters
    checkAnagram(string1, string2)


    # chkAnagram("tat", "bat")
    # chkAnagram("stressed", "desserts")