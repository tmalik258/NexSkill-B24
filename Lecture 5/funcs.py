x = 12
y = 2

sum_result = x + y


k = 24
z = 45

sum_result = k + z


i = 89
j = 45

sum_result = i + j


# no argument functions
def add_static():
    m = 45
    n = 23

    sum_result = m + n
    print(sum_result)


# add_static()
# add_static()
# add_static()
# add_static()
# add_static()
# add_static()

def random():
    pass

# two arguments functions
def add_dynamic(m, n): # arguments or parameters
    sum_result = m + n

    print(sum_result)


add_dynamic(1, 2)
add_dynamic(5, 115)
add_dynamic(45, 23)


# write 4 functions
# multiplication
# division
# subtraction
# remainder


# write a python program that takes a color as input and prints and action:

# "Red" -> "Stop"
# "Yellow" -> "Get Ready"
# "Green" -> "Go"
# Any other color -> "Invalid color"

age = 20

if (age > 18) or (age < 60):
    print("Eligible to vote")


# write a program that checks whether a person is eligible for loan or not based on the following conditions:
# 1. Age should be between 25 and 60
# 2. Income should be greater than 50000


# if both conditions true then print "Eligible for loan"
# else print "Not Eligible for loan"

if not (age < 25):
    print("test")

name = "Ali"

if not (name == "Talha" or name == "Hassnain"):
    print("you are a student")
else:
    print("you are a teacher")