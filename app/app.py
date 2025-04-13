from flask import Flask, jsonify, request

app = Flask(__name__)

# Root route
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask API!"})

# Example GET route
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, world!"})

# Route that handles POST request with JSON payload
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload received"}), 400
    return jsonify({"you_sent": data})

# Route that adds two numbers
@app.route('/api/add', methods=['POST'])
def add():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"error": "Please provide 'a' and 'b' in the JSON payload"}), 400
    try:
        result = float(data['a']) + float(data['b'])
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid numbers provided"}), 400

# Custom 404 error handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Route not found"}), 404

# Custom 500 error handler
@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
