# A student class to add students to a web application

# create an empty list
students = []
class Student:
    '''
    instance variable school_name
    init, str, capitalize name and school name functions
    '''
    school_name = "Springfield High School"

    def __init__(self, name, last_name, student_id = 332):
        self.name = name
        self.last_name = last_name
        self.student_id = student_id
        students.append(self)

    # since the init, initializes the object in the heap, 
    # if we want to print it, we need to convert it to a string
    def __str__(self):
        return "Student " + self.name   

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name