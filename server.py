from flask import Flask, request

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()  # Assuming JSON data in the POST request
    first = data.get('first')
    second = data.get('second')
    if first is None or second is None:
        return "Missing 'first' or 'second' in the request data", 400
    try:
        result = float(first) + float(second)
        return str(result)
    except ValueError:
        return "Invalid input data, 'first' and 'second' should be numbers", 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()  # Assuming JSON data in the POST request
    first = data.get('first')
    second = data.get('second')
    if first is None or second is None:
        return "Missing 'first' or 'second' in the request data", 400
    try:
        result = float(first) - float(second)
        return str(result)
    except ValueError:
        return "Invalid input data, 'first' and 'second' should be numbers", 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
