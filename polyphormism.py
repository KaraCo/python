## Inheritance

# Like in java, inheritance allows to bring functions and attributes from other classes

# this class will inherit all functions and attributes from the Alumnus class
# the parent class, the one from which the functions will be inherited, goes in parenthesis

# To use a class created in another file, use: from filename import TheClass

from classes import Alumnus

class HighSchoolReunion(Alumnus):
    school_name = "Springfield High School"     # We can override attributes/functions

    def get_school_name(self):
        original_value = super().get_name_capitalize()
        return original_value + " HS Student"

james = HighSchoolReunion("james")
print(james.get_name_capitalize())
print(james.get_school_name())
print(james.student_id)