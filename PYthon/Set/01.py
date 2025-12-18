 # set are not allow duplicate element set are the Unique  and unordered element
 # DONT ALLOW DUPLICATE ELEMENT >> NOT MOUNTAIN ANY order and it wil not indexed

 # Define the set {}
s = {}
print(type(s)) # dictionary
s1 = {1,2,3,4,5}
print(type(s1)) # Set

s2 = {1,2,3,4,5,"Amar","amar", "Amar"}
print(s2)

list1  = [1,3,4,4,4,5,6,67,3245,5,5,435435,66]
print(set(list1))
for i in s2:
    print(i)
print(len(s2))
s2.add("Kumar")
print(s2)
print(s2.pop())
print(s2.remove(2))
print(s2)

# 