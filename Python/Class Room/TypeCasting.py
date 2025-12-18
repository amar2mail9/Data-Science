# One data type to another data type is known as type casting

a = "5" # this is string
type(a) # string

b = 2 # int
type(b) # int

# Type casting is two type : 1. implicit    2. Explicit
x = 2 # int (implicit type) : Auto python understand is know as implicit

# Explicit Type: convert data type using in  built in function

# this is convert float ----> integer
x1 = 22.5
y = int(x1) # int

# convert string -----> Integer ? float

x2 = '234.5'
y1 = float(x2) # float 
y2 = int(y1)

#  boolean value
bool(0) # false
bool(1) # true


# string / character -----> int / float 
# Error : not convert 
name = "Alex"

type(name)

int(name) # Error
float(name) # Error