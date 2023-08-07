import os
import openai

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from src.prompt_template import template_string, style

try:
    openai.api_key = os.environ['OPENAI_API_KEY']
    chat = ChatOpenAI(temperature=0.0)
except KeyError:
    print('Error: OPENAI_API_KEY environment variable not set.')
    # raise Exception("OPENAI_API_KEY environment variable not set.")

prompt_template = ChatPromptTemplate.from_template(template_string)


def chat_user(customer_email):
    customer_messages = prompt_template.format_messages(
        style=style,
        text=customer_email)
    customer_response = chat(customer_messages)
    return customer_response.content
