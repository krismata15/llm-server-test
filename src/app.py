from flask import Flask, jsonify, request
from dotenv import load_dotenv

from llm_handler import chat_user

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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
