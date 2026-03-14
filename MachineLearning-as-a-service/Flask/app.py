from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Endpoint test
    """
    return "Hello World"

@app.route('/nuclio')
def hello_nuclio():
    """
    Endpoint test
    """
    return "Hello Nuclio"

@app.route('/predict', methods=['POST']) 
def print_square(): 
    """
    Endpoint test
    """
    data = request.get_json(force=True)
    recieved_value = int(data.get('numero'))
    print(recieved_value) 
    return str(recieved_value**2)

@app.route('/predictget') 
def print_square2(): 
    """
    Endpoint test
    """
    numero = request.args.get('numero')
    recieved_value = int(numero) 
    print(recieved_value) 
    return str(recieved_value**2)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)