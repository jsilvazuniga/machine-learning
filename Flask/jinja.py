# Building URL dinamically in Flask
# Varialbe Rules in Flask
# Building a Jinja2 Template Engine in Flask
'''
{{ variable_name }} is used to display the value of a variable in the template.
{% for item in items %} is used to create a loop that iterates over a list of items and displays them in the template.
{% if condition %} is used to create a conditional statement that displays different content based on the value of a variable.
{% extends "base.html" %} is used to create a template that inherits from a base template, allowing you to reuse common elements across multiple pages. 

'''


from flask import Flask, render_template, request, redirect, url_for
'''
This is a simple Flask application that defines a single route and returns a greeting message.
'''
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><body><h1>Welcome to my Flask app!</h1></body></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission here
        print("Form submitted!")
        print(request.form)  # Print the form data to the console
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        # For now, just print the form data to the console
        return f"Name: {name}, Email: {email}, Message: {message}"
    return render_template("form_contact.html")

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Handle form submission here
        print("Form submitted!")
        print(request.form)  # Print the form data to the console
        name=request.form['name']
        email=request.form['email']
        calification=request.form['calification']
        message=request.form['message']
        # For now, just print the form data to the console
        #return f"Name: {name}, Email: {email}, Message: {message}"
        print(f"Name: {name}, Email: {email}, Calification: {calification}, Message: {message}")
    #return render_template("form_contact.html")
    return redirect(url_for("success2", score=calification ))

# Variable Rules in Flask
@app.route("/success/<int:score>", methods=["GET"])
def success(score):
    res=""
    if score >= 50:
        res="Passed"
    else:
        res="Failed"    
    #return f"Success! Your score is {score} and you have {res}."
    return render_template("result.html", score=score, result=res)

# Variable Rules in Flask
@app.route("/successres/<int:score>", methods=["GET"])
def success2(score):
    res=""
    if score >= 50:
        res="Passed"
    else:
        res="Failed"    
    exp = {"score": score, "result": res}
    return render_template("result1.html", results=exp)



if __name__ == "__main__":
    app.run(debug=True)