from flask import Flask, render_template
'''
This is a simple Flask application that defines a single route and returns a greeting message.
'''
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><body><h1>Welcome to my Flask app!</h1></body></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)