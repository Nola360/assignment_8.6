#Akinola Daramola Jr
#Programming Exercise 7.6
#Due Date: 08/03/2022

"""
Larger Than n
In a program, write a function that accepts two arguments: a list, and a number n.
Assume that the list contains numbers.
The function should display all of the numbers in the list that are greater than the number n.

"""

#Importing random module
import random

#Declaring value of n variable 0 - 20
n = random.randint(0, 20)
#Displaying value of n variable
print(f"Variable n: {n}")

#Initializing number_element
number_elements = 0

#Creating empty list number_list 
number_list = []

#Defining main() function to invoke numberGenerator() function
def main():
    #Invoking numberGenerator() function with two glocal parameters
    numberGenerator(number_list, n)

#Defining numberGenerator() function
def numberGenerator(number_list, n):
    #Using for loop to iterate through range of 0 - 10
    for numbers in range(0,10):

        #Declaring random value of numbers variable 0 - 40
        numbers = random.randint(0, 40)

        #Appending numbers to empty list as elements
        number_list.append(numbers)

        #Sorting elements from < to >
        number_list.sort()
    #Displaying list of elements
    print("List of numbers:", number_list)

    #Creating empty list called greater_than
    greater_than = []

    #Using for loop to iterate through conditional
    for elements in number_list:

        #If statement for elements greater than n variable
        if elements > n:
            #Appending all elements greater than n variable in list
            greater_than.append(elements)
    #DIsplaying all numbers in list greater than n variabke in list
    print(f"Numbers greater than {n}.", greater_than)

#Invoking main() function to start program
main()




