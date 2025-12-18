# Loops allows you to repeated executed a block of code , while and for loop 
# 
# While loop: repeatedly excutes 

n = 7
i = 1

while i < n: #true
    print(i)
    i = i+1

'''
# How do While loop works

step by step

step 01 check i is less then 7 then code execute i = 1

step 02 check i is less then 7 then code execute i = 2
step 03 check i is less then 7 then code execute i = 3
step 04 check i is less then 7 then code execute i = 4
step 05 check i is less then 7 then code execute i = 5
step 06 check i is less then 7 then code execute i = 6
step 07 check i is less then 7 then code terminated i = 7
'''

count = 5

while count > 0:
    print(count)
    count = count -1
    if count ==3:
        break
else:
    print("This will be executed ")


# check even odd number

number  = int(input("Enter A Number"))

while number > 1:
  
    if number % 2 == 0:
        print(f"{number} is even")
        
    else:
        print(f"{number} is odd")
    number -= 1
  
        

