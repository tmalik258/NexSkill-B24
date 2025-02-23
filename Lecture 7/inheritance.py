class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        print(f'{self.name} is walking')
    
    def talk(self):
        print(f'{self.name} is talking')
    
    def display(self):
        print(f'Name: {self.name}, Age: {self.age}')

# p1 = Person('Ali', 20)
# p1.display()
# p1.walk()
# p1.talk()


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self):
        print(f'{self.name} is studying')
    
    def enroll(self):
        print(f'{self.name} is enrolled with student id: {self.student_id}')
    
    def display(self):
        super().display()
        print(f'Student ID: {self.student_id}')


st1 = Student("Ali", 20, 123)

st1.study()
st1.talk()
st1.enroll()
st1.walk()
st1.display()