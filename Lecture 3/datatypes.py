# string
# int
# float
# boolean

# list
# tuple
# dictionary

# None
# undefined


test = 'Hello World' # array of chars / list of chars
x = 45 # int
y = 43 # int
z = 2.5 # float
a = True # boolean
b = False # boolean


result = x / y
# print(result)
# print(45)
# print(b)

# area of triangle
# area of circle


students = ['ali', 'ahmed', 'khan'] # list

students[1] = 'talha'

# = means assign to - assignment operator

print(students[1]) # undefined or error


# Task 1 - Update any value in a list
# Task 2 - Update any value in a dict

talha_teacher = {
    "name": ["talha", "ahmed", "khan"],
    "age": {
        "talha": 20,
        "ahmed": 21,
        "khan": 22
    },
    "city": "Lahore",
    "country": "Pakistan",
}

students = [
    {
        "name": "ali",
        "age": 20
    },
    {
        "name": "usman",
        "age": 21
    },
    {
        "name": "khan",
        "age": 22,
        "marks": [100, 86, 22]
    },
]

# print(students[1]["age"])


# print second student age from list of students

# print('flskjdf')


# dictionary or object

# nested datatypes
# nested loops


# tuple - immutable

teacher = {
    "name": "talha",
    "age": 22,
    "city": "lahore"
}

teacher = ["lahore", 22, "talha"]

print("teacher name is ", teacher[0])


test_list  = [10, 30, 20] # mutable
# test_list[1] = 100
test_tuple = (10, 20, 30) # immutable

print(test_tuple[2])

test_list.append(25) # method - to add value at the end of the list
# test_tuple.append(25)

test_list.pop() # to remove last value
test_list.remove(20) # to remove first occurence of value
test_list.remove(10)

test_list.insert(1, 100)


# to add multiple values in a list
test_list = test_list + [45, 23, 78]

print(test_list)

test_list.extend([415, 233, 728])
print(test_list)

print(test_list[1])

print(test_list[2:5])
print(test_list[2:-1])
print(test_list[2:])
print(test_list[:3]) # slicing

names = ['Alice', 'bob', 'Charlie', 'david']

# create a new reversed list or reversed_names
# that contains the elements in reverse order
# using slicing and print it
# reversed_names

# print(test_list[-1:5:-2])

test_list_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


print(test_list_2[-1:5:-1])
# -1:5:-2
# 100, 90, 80, 70
