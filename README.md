# LLM server

Server with Langchain Language Model (LLM) for language generation using Flask.

## Installation

A OPENAI api key is required. Create a file named `.env` with the following content:

```dotenv
OPENAI_API_KEY=<your-openai-api-key>
```

If a key is not provided, the server will print and error and continue working without LLM capabilities.

### Local
```bash
pip install -r requirements.txt
python main.py
```

### Docker

```bash
docker build -t kdata/llm-server-test .
```
```bash
docker run -p 4000:4000 -d kdata/llm-server-test
```

## Initial implementation

This implementation follows the tutorial [LangChain for LLM Application Development](https://learn.deeplearning.ai/langchain/lesson/2/models,-prompts-and-parsers).