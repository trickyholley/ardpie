from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from services.claude import ClaudeService

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"

@app.route('/api/bake-budget-item', methods=['POST'])
def stream_logs():
    prompt = request.json.get("prompt", "")

    claude_service = ClaudeService()

    response_stream = claude_service.generate_response(prompt)

    def generate():
        for text in response_stream:
            yield text

    return Response(generate(), content_type="text/plain")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
