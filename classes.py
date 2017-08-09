## Creating Classes in Python

# classes are defined with the keyword class and the class name starts with Capital Letter like in Java

class Test:
    pass        # keyword that tells python to do nothing. It's like a place holder

# to create a new instance of a class, like in Java need to declare a variable and pass the class

new_test = Test()
print(new_test)     # this will print the location in memory for this object.(heap segment)


# The following code will create a Student class

students = []   # create an empty list to keep the students

# the class has one function, which takes two parameters.
# the self parameter is how we can use the function inside the class, it's like 'this' in java

class Student:
    def add_student(self, name, student_id = 123):
        student = {"name":name, "student_id":student_id}
        students.append(student)

# create a new Student object/instance and use the function

estudiante = Student()
estudiante.add_student("Katarina")

print(students)

# Another way to create a class that initializes an object and given parameters is to use the __init__ function

students_list = []
class UpdatedStudent:
    def __init__(self, name, student_id = 234):
        student_dict = {"name": name, "student_id": student_id}
        students_list.append(student_dict)

    # in order to avoid printing the memory reference/heap when calling the new object, we use __str__
    # which converts the location to a string.

    def __str__(self):
        return "UpdatedStudent"

new_student = UpdatedStudent("Roxanne")
print(students_list)
print(new_student)


# Another way to create a class is to avoid using the dictionary and using the 'self' keyword instead
# instance variables can also be added to the class. These are static attributes. They DO NOT change = Static.
# Instance variables inside a class are available to all the new instances/objects created inside the class

new_student_list = []

class Alumnus:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=890):
        self.name = name
        self.student_id = student_id
        new_student_list.append(self)
    
    def __str__(self):
        return "Alumnus " + self.name
    
    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

mark = Alumnus("mark")
print(mark)
print(mark.get_name_capitalize())