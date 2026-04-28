"""Question 1: The Basic Counter

Use a for loop and the range() function to print the numbers from 1 to 50 (inclusive).

Goal: Practice the syntax of range(start, stop).
"""
for i in range(1, 51):
         print(i, end=" ")
"""
Question 2: The Multiplier

Write a program that asks the user for a number and then prints the "multiples" of that number from 1 to 10.

Example Output (if user enters 5): 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
"""
number = int(input("Please Enter Any Number : "))

for i in range(1, 11):
    print(number * i , end=" ") 
"""
Question 3: Square Numbers

Create a loop that calculates and prints the square (n^2) of every number from 0 to 4.
"""
for i in range(0, 5):
 print(i**2)   
