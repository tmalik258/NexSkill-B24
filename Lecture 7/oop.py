# object oriented programming
# class # blueprint # attributes # methods
# objects

class Cat: # encapsulation
    def __init__(self, l, t, n): # constructor
        self.legs = l
        self.tail = t
        self.name = n

    def meow(self): # methods
        print("meow")
    
    def play(self):
        print("playing")
        # global test
        # test = 45
    
    def sleep(self):
        print("sleeping")

    def display(self):
        # a = "hello"
        # print(f"{a} world") # f string
        print(f"Name: {self.name}, Legs: {self.legs}, Tail: {self.tail}")


cat1 = Cat(4, True, "Tiger") # object creation
cat2 = Cat(3, True, "Alex")
cat3 = Cat(4, False, "Snow")

# cat1.play()
# cat1.display()
# cat2.dispaly()

cat1.display()
cat2.display()
cat3.display()

# cat2.sleep()
# cat2.meow()

# cat1.meow()
# cat1.sleep()


# def sleep():
#     print("sleeping")


# sleep()


# Make a class Student
# having attributes name, student_id, age, marks
# and methods enroll, pay_fees, studying

# self
