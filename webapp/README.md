# Usign Flask to create a web application with python

[**Flask**](http://flask.pocoo.org/docs/0.12/) is a web microframework to power web applications. Although, Django is the most famous web framework, Flask it's a microframework that is generally easier to use than Django as it requires only a few lines of code to execute:

```from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

Using jinja2, which is a template engine for Python, we can add logic code inside the html template.