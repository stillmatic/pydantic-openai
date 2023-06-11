"""Completion related APIs.

Related: https://platform.openai.com/docs/api-reference/completions/create
"""
from enum import Enum
from typing import List, Dict, Union, Optional
from pydantic import BaseModel

from .common import Usage

# GPT3 models provided by OpenAI for text-based tasks
class GPT3Models(str, Enum):
    GPT432K0314 = "gpt-4-32k-0314"
    GPT432K = "gpt-4-32k"
    GPT40314 = "gpt-4-0314"
    GPT4 = "gpt-4"
    GPT3Dot5Turbo0301 = "gpt-3.5-turbo-0301"
    GPT3Dot5Turbo = "gpt-3.5-turbo"
    GPT3TextDavinci003 = "text-davinci-003"
    GPT3TextDavinci002 = "text-davinci-002"
    GPT3TextCurie001 = "text-curie-001"
    GPT3TextBabbage001 = "text-babbage-001"
    GPT3TextAda001 = "text-ada-001"
    GPT3TextDavinci001 = "text-davinci-001"
    GPT3DavinciInstructBeta = "davinci-instruct-beta"
    GPT3Davinci = "davinci"
    GPT3CurieInstructBeta = "curie-instruct-beta"
    GPT3Curie = "curie"
    GPT3Ada = "ada"
    GPT3Babbage = "babbage"

# Codex models provided by OpenAI for code-specific tasks
class CodexModel(str, Enum):
    CodexCodeDavinci002 = "code-davinci-002"
    CodexCodeCushman001 = "code-cushman-001"
    CodexCodeDavinci001 = "code-davinci-001"

class PromptType:
    @staticmethod
    def checkPromptType(prompt: Union[str, List[str]]) -> bool:
        return isinstance(prompt, str) or isinstance(prompt, list)

class CompletionRequest(BaseModel):
    model: str
    prompt: Optional[Union[str, List[str]]] = None
    suffix: Optional[str] = None
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    n: Optional[int] = None
    stream: Optional[bool] = None
    logprobs: Optional[int] = None
    echo: Optional[bool] = None
    stop: Optional[List[str]] = None
    presence_penalty: Optional[float] = None
    frequency_penalty: Optional[float] = None
    best_of: Optional[int] = None
    logit_bias: Optional[Dict[str, int]] = None
    user: Optional[str] = None

class LogprobResult(BaseModel):
    tokens: List[str]
    token_logprobs: List[float]
    top_logprobs: List[Dict[str, float]]
    text_offset: List[int]

class CompletionChoice(BaseModel):
    text: str
    index: int
    finish_reason: str
    logprobs: LogprobResult

class CompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[CompletionChoice]
    usage: Dict[str, int]