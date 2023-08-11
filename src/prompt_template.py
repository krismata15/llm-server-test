customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

style = """American English \
in a calm and respectful tone
"""

prompt = f"""Translate the text \
that is delimited by triple backticks 
into a style that is {style}.
text: ```{customer_email}```
"""

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

example_trivia_template = """Generate a {trivia_subject} trivia
    of {trivia_question_number} random question with {trivia_options_number} options
    and show the answer 
    with a difficulty of {trivia_difficulty} existing three types of difficulty: easy, medium and hard.
    Show in json format array, without markdown, the following fields:
    'question',
    'options',
    'answer',
    """

trivia_topic_examples = [
    "Star Wars 🌌",
    "Harry Potter 🧙‍♂️",
    "Lord of the Rings 🗡️",
    "Marvel Cinematic Universe 🦸‍♂️",
    "DC Extended Universe 🦸‍♀️",
    "The Simpsons 😂",
    "Game of Thrones 👑",
    "The Big Bang Theory 🤓",
    "Friends 👬",
    "The Office 😂",
    "Messi ⚽️",
    "C. Ronaldo ⚽️",
    "LeBron James 🏀",
    "Michael Jordan 🏀",
    "Tiger Woods ⛳️",
    "Usain Bolt 💨",
]
