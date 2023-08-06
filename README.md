# LLM server

Server with Langchain Language Model (LLM) for language generation using Flask.

## Installation

### Local
```bash
pip install -r requirements.txt
python app.py
```

### Docker

```bash
docker build -t kdata/llm-server-test .
```
```bash
docker run -p 4000:4000 -d kdata/llm-server-tes
```

## Initial implementation

This implementation follows the tutorial [LangChain for LLM Application Development](https://learn.deeplearning.ai/langchain/lesson/2/models,-prompts-and-parsers).