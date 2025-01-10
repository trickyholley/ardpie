from flask import Flask
from flask_cors import CORS
from services import user_blueprint  # Replace with the actual package name

# Create a Flask app instance
app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000"}})

# Register the user blueprint
app.register_blueprint(user_blueprint, url_prefix='/api')


# Define a GET endpoint
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"


# Run the server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
