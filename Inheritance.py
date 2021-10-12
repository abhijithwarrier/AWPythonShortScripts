# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO DEMONSTRATE INHERITANCE IN PYTHON
#
# Inheritance is capability of one class to derive or inherit properties from another class.
# The benefits of inheritance are:
# - It represents real-world relationships well.
# - It provides reusability of a code. We don’t have to write the same code again and again.
#   Also, it allows us to add more features to a class without modifying it.
# - It is transitive in nature, which means that if class B inherits from another class A,
#   then all the subclasses of B would automatically inherit from class A.

# Creating a parent class called Base():
class Base():
    # Defining function named sum() with arguments a and b
    def sum(self, a, b):
        # Returning the sum of a and b
        return a+b

# Creating a child class called Child() inheriting parent Base Class
class Child(Base):
    # Defining function named mul() with arguments c and d
    def mul(self, c, d):
        # Returning the product of c and d
        return c*d

# Creating the object of Child() class called childObj
childOBJ = Child()
# Accessing mul() function defined in child class.
print("\nMULTIPLICATION : ", childOBJ.mul(6, 4))
# Accessing sum() from parent class. Function can be accessed because of INHERITANCE
print("\nADDITION : ", childOBJ.sum(5, 5))