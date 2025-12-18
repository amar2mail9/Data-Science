'''
Docstring for Sum
4. Sum of Numbers

Take an integer N and find the sum of numbers from 1 to N.

Concepts: loop, accumulator variable
'''


user_input = int(input("Enter Number: "))

sum = 0

while user_input >= 1:
    sum += user_input
    user_input -=1

print(sum)