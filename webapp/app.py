
# Using Flask

from flask import Flask, render_template, redirect, url_for, request

from  student import Student

students = []

app = Flask(__name__)

# The methods passed in the @app.route, correspond to the functions the web pages will handle
# both GET or display the information that is entered by the user when the browser fetches the page
# POST when adding new students to the form. 

@app.route("/", methods = ["GET", "POST"])  # the requests that the web app form will handle

#if the the request is POST, get the student name, id, and last name from the form on the .html form
def students_page():
    if request.method== "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        #This time ONLY, create a new student variable to keep the id, name and last name 
        #and appended to the empty list.  For this situation a DB is betters, so all the data is not saved in the RAM'''
        
        new_student = Student(name = new_student_name, last_name = new_student_last_name, student_id = new_student_id)
        students.append(new_student)

        #redirect the user to the same page they came from'''
        return redirect(url_for("students_page"))

    #render the html page and pass the list''' 
    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
