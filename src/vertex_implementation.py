import json
import vertexai

from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain

vertexai.init(project="proyecto-llm", location="us-central1")


def trivia_text_llm_function(trivia_subject, trivia_question_number=1, trivia_options_number=4, previous_questions=[]):
    template = """Generate a {trivia_subject} trivia
    of {trivia_question_number} random question with {trivia_options_number} options
    and show the answer 
    with a difficulty of {trivia_difficulty} existing three types of difficulty: easy, medium and hard.
    
    Don't repeat the questions that have already been asked. The already asked questions are:
    "{previous_questions}"
    
    Show in json format, without markdown, the following fields:
    'question',
    'options',
    'answer',
    """
    prompt = PromptTemplate(template=template,
                            input_variables=["trivia_subject",
                                             "trivia_options_number",
                                             "trivia_difficulty",
                                             "trivia_question_number",
                                             "previous_questions"])

    llm = VertexAI(model_name="text-bison@001",
                   max_output_tokens=512,
                   temperature=0.8,
                   top_p=0.8,
                   top_k=40,
                   verbose=False)

    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=False)

    response = llm_chain.run({'trivia_subject': trivia_subject,
                              'trivia_options_number': trivia_options_number,
                              'trivia_difficulty': 'hard',
                              'trivia_question_number': trivia_question_number,
                              'previous_questions': "\"\n \"".join(previous_questions),
                              })

    clean_response = response.replace("\n", "").replace("json", "").replace("```", "")
    y = json.loads(clean_response)
    return y


# LLMChain
def test_trivia_llm_function(trivia_subject, trivia_question_number=2, trivia_options_number=4):
    template = """Generate a {trivia_subject} trivia
    of {trivia_question_number} random question with {trivia_options_number} options
    and show the answer 
    with a difficulty of {trivia_difficulty} existing three types of difficulty: easy, medium and hard.
    Show in json format array, without markdown, the following fields:
    'question',
    'options',
    'answer',
    """
    prompt = PromptTemplate(template=template,
                            input_variables=["trivia_subject",
                                             "trivia_options_number",
                                             "trivia_difficulty",
                                             "trivia_question_number"])

    llm = VertexAI(model_name="text-bison@001",
                   max_output_tokens=512,
                   temperature=0.1,
                   top_p=0.8,
                   top_k=40,
                   verbose=False)

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    response = llm_chain.run({'trivia_subject': trivia_subject,
                              'trivia_options_number': trivia_options_number,
                              'trivia_difficulty': 'hard',
                              'trivia_question_number': trivia_question_number,
                              })
    clean_response = response.replace("\n", "").replace("json", "").replace("```", "")
    y = json.loads(clean_response)
    return y
