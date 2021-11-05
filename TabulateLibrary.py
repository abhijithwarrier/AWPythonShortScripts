# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO DISPLAY DATA IN TABULAR FORM IN THE TERMINAL USING prettytable LIBRARY
#
# prettytable is a simple Python library for easily displaying tabular data
# in a visually appealing ASCII table format.
# It was inspired by the ASCII  tables used in the PostgreSQL shell psql.
# Many aspects of a table, such as the width of the column padding, the
# alignment of text, or the table border can be controlled. We can sort data.
# It can be used to create relational tables in Python
#
# The module can be installed using the command - pip install prettytable

# Importing the library
from prettytable import PrettyTable

# Initializing table using PrettyTable() method
sample_tample = PrettyTable()

# Setting header names (Columns) of table to the field_name attribute
sample_tample.field_names = ['SERIAL No', 'NAME', 'CITY']

# Adding list of rows to the table at same time using add_rows method
sample_tample.add_rows(
    [
        ['01', 'Abhi', 'Cochin'],
        ['02', 'Dhiraj', 'Kolkata'],
        ['03', 'Jay', 'Chennai'],
        ['04', 'Maddy', 'Banglore'],
        ['05', 'Yash', 'Mumbai']
    ]
)
# Rows can also be added one at a time using the add_row() method

# Prining the newly create table
print("\nTABLE CREATED USING prettytable LIBRARY\n")
print(sample_tample)

# Clearing the table records using the clear_rows() method of table object
sample_tample.clear_rows()

# clear_rows() will clear all the table records. Only column names will remain
# Printing the table again
# Prining the newly create table
print("\nTABLE AFTER CLEARING THE TABLE RECORDS\n")
print(sample_tample)
