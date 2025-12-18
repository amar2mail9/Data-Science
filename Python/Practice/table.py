'''
Docstring for table
5. Multiplication Table

Take a number and print its multiplication table up to 10.

Concepts: for loop, arithmetic operations

'''

# using for loop 
user_input = int(input("Enter a Number : "))

for i in range(10):
    print(f"{user_input} X {i  + 1} = {user_input * ( i + 1 )}")


print("<========== Using While Loop ==========>")
i = 1
while i <=10:
    print(f"{user_input} X {i} = {user_input * i}")   
    i += 1
