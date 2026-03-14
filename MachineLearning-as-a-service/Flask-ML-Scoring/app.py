import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

model = None
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def hello_world():
    """
    Endpoint test
    """
    return "Hello World"


@app.route('/predict', methods=['POST'])
def predict():
    parameters = request.get_json(force=True)
    f1 = int(parameters['age'])
    f2 = int(parameters['income'])
    f3 = int(parameters['female'])
    f4 = int(parameters['male'])
    spending_score = model.predict([[f1, f2, f3, f4]])[0]
    print(spending_score)
    return jsonify(spending_score)

if __name__ == '__main__':
    app.run(host='0.0.0.0')