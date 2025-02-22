# object oriented programming
# class # blueprint # attributes # methods
# objects

class Cat: # encapsulation
    legs = 4 # attributes
    tail = True
    name = "Tiger"

    def meow(self): # methods
        print("meow")
    
    def play(self):
        print("playing")
        # global test
        # test = 45
    
    def sleep(self):
        print("sleeping")

    def display(self):
        print(self.name)


cat1 = Cat()
cat2 = Cat()

cat1.play()

cat1.display()

cat2.dispaly()

print(cat1.legs)
print(cat2.tail)
print(cat2.name)

cat2.sleep()
cat2.meow()

cat1.meow()
cat1.sleep()


# def sleep():
#     print("sleeping")


# sleep()


# Make a class Student
# having attributes name, student_id, age, marks
# and methods enroll, pay_fees, studying

# self
