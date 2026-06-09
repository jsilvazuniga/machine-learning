from flask import Flask, render_template, request
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

if __name__ == "__main__":
    app.run(debug=True)