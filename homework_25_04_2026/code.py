'''1. Count 1 to N using while
Write a program that takes an integer N and prints numbers from 1 to N using a while loop.
Example: if N = 5, output should be 1 2 3 4 5.
'''
N = int(input("Enter a number: "))

i = 1
while i <= N:
    print(i)
    i +=1

'''2. Sum of first N numbers
Take an integer N and calculate the sum from 1 to N using a while loop and a counter variable.
Example: if N = 5, output should be 15.
'''
N = int(input("Enter a number: "))

i = 1
total = 0
while i <= N:
    total = total + i
    i +=1
print(total)
   
'''3. Even numbers in a range
Take two integers start and end, then print all even numbers between them (inclusive) using a while loop.
Example: start = 3, end = 10 → 4 6 8 10.
'''
start_number = int(input("Enter Start Number: "))
end_number = int(input("Enter End Number: "))

while start_number <= end_number:
    if start_number % 2 ==0:
        print(start_number)
    start_number +=1
    
 '''   4. Input until 0 (sentinel loop)
Keep taking integer input from the user until they enter 0. After loop ends, print:
a. total numbers entered (excluding 0)
b. sum of those numbers
'''
number = int(input("Please Enter Number ( Integer) : "))
count = 0
total = 0
while number != 0:
    total +=number
    count +=1
    number = int(input("Please Enter Number ( Integer) : "))
print(f"total Sum : {total}")
print(f"total Count : {count}")
