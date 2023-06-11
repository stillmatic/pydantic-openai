# pydantic-openai

Pydantic models for OpenAI's API. These make it easier to construct requests and parse responses, as well as set up API-compatible servers.

Making requests is explicitly out of scope.

This is mostly translated from [sashabaranov/go-openai](https://github.com/sashabaranov/go-openai/tree/master), by ChatGPT. I welcome translating the rest over, I just don't really use the other API's.

# Usage

See the package on [PyPI](https://pypi.org/project/pydantic-openai/). 

```bash
pip install pydantic-openai
```

```python
from pydantic_openai import ChatCompletionRequest
```