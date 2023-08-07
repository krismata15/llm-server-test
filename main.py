import os

from flask import Flask, jsonify, request
from dotenv import load_dotenv

from src.llm_handler import chat_user
from src.vertex_implementation import test_trivia_llm_function

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})


@app.route('/chat', methods=['POST'])
def chat():
    request_data = request.get_json()
    chat_data = request_data['input']
    response = chat_user(chat_data)
    return jsonify({'response': response})


@app.route('/generate-trivia', methods=['GET'])
def generate_trivia():
    response = test_trivia_llm_function("star wars")
    return jsonify({'response': response})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
