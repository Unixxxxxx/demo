from flask import Flask
import socket  # <- ADD THIS LINE

app = Flask(__name__)

@app.route('/')
def hello():
    container_id = socket.gethostname()
    return f"Hello, {container_id}"

if __name__ == '__main__':
    app.run(debug=True)
