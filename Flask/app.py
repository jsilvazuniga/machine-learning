from flask import Flask
'''
This is a simple Flask application that defines a single route and returns a greeting message.
'''
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my Flask app!, this is amazing :D :D"

@app.route("/index")
def index():
    return "This is the index page!"

if __name__ == "__main__":
    app.run(debug=True)