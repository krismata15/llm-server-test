import os

from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_cors import CORS

from src.llm_handler import chat_user
from src.prompt_template import trivia_topic_examples
from src.vertex_implementation import test_trivia_llm_function, trivia_text_llm_function

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})


@app.route('/chat', methods=['POST'])
def chat():
    request_data = request.get_json()
    chat_data = request_data['input']
    response = chat_user(chat_data)
    return jsonify({'response': response})


@app.route('/generate-trivia', methods=['POST'])
def generate_trivia():
    request_data = request.get_json()

    trivia_topic = request_data.get('trivia_topic', None)

    if trivia_topic is None:
        return jsonify({'message': 'Please provide a trivia topic'}), 400

    messages = request_data.get('previous_questions', [])

    if len(messages) > 10:
        return jsonify({'response': 'You have reached the maximum number of questions'}), 400

    response = trivia_text_llm_function(trivia_topic, previous_questions=messages)

    return jsonify({'data': {'trivia_question': response}})


@app.route('/trivia-topics', methods=['GET'])
def get_trivia_topics():
    return jsonify({'data': {'trivia_topics': trivia_topic_examples}}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
