'''
Docstring for Even_Odd


2. Even Numbers Using while

Take a number N from the user and print all even numbers from 1 to N using a while loop.

Concepts: while loop, conditionals

'''

user_input = int(input("Enter Number: "))

while user_input > 1:
    if user_input % 2 == 0:
        print(f"Even Number: {user_input}")
        
    user_input -=1
