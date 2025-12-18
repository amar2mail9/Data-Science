'''
6. Odd or Even Counter

Take N as input and count how many odd and even numbers exist between 1 and N.

Concepts: loops, if-else, counters
'''

user_input = int(input("Enter Number: "))

print("---------- User for Loop ----------")
even_count = 0
odd_count = 0 
for i in range(user_input ):
    if (i+1) % 2 == 0:
        even_count += 1
    
    if (i+1) % 2 != 0:
        odd_count += 1
print(f"Number of Even count  : {even_count} ")
print(f"Number of Odd count  : {odd_count} ")

print('\n========= While Loop ==========')

even_count = 0
odd_count = 0 
while user_input >=1:
    #  for Even Number
    if (user_input % 2 == 0 ):
        even_count += 1

        # for odd number
    if (user_input % 2 != 0 ):
        odd_count += 1

    user_input -= 1

print(f"Number of Even count  : {even_count} ")
print(f"Number of Odd count  : {odd_count} ")