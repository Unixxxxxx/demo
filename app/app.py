from flask import Flask, jsonify, request

app = Flask(__name__)

# Example route
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

# Route that handles POST request with JSON payload
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
