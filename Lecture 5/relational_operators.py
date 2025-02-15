test = "hello" # assignment operator


print(test == "world") # equality operator


print(test != "world") # not equal to operator

age = 20

print(age > 18) # greater than operator
print(age < 18) # less than operator
print(age >= 18) # greater than or equal to operator
print(age <= 18) # less than or equal to operator


if age >= 18:
    print("eligible to enroll in this course")
else:
    print("not eligible to enroll in this course") # if-else statement

print("hello world")

# marks = input("Enter your marks: ") # input function
marks = int(input("Enter your marks: ")) # type casting, 

print("your marks are: ", type(marks))


marks_string = "45"

marks_int = int(marks_string) # type casting or data type casting

print("your marks are: ", type(marks_string))
print("your marks are: ", type(marks_int))

# ask the user for a number and print "Positive" if the number is positive


temperature = 45

temperature = (temperature % 2) == 0


if temperature > 30:
    print("Temperature is too hot.")
elif temperature < 0:
    print("Temperature is too cold.")
elif temperature < 10:
    print("Temperature is freezing.")


if temperature > 30:
    print("Temperature is too hot.")
if temperature < 0:
    print("Temperature is too cold.")
if temperature < 10:
    print("Temperature is freezing.")
