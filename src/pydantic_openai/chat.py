"""Chat completion related APIs.

Reference: https://platform.openai.com/docs/api-reference/completions
"""
from typing import List, Dict, Optional
from enum import Enum
from pydantic import BaseModel, Field
from .common import Usage


class ChatMessageRole(str, Enum):
    System = "system"
    User = "user"
    Assistant = "assistant"

class ChatCompletionMessage(BaseModel):
    role: ChatMessageRole
    content: str
    name: Optional[str] = Field(None, alias="name")

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatCompletionMessage]
    max_tokens: Optional[int] = Field(None, alias="max_tokens")
    temperature: Optional[float] = Field(None, alias="temperature")
    top_p: Optional[float] = Field(None, alias="top_p")
    n: Optional[int] = Field(None, alias="n")
    stream: Optional[bool] = Field(None, alias="stream")
    stop: Optional[List[str]] = Field(None, alias="stop")
    presence_penalty: Optional[float] = Field(None, alias="presence_penalty")
    frequency_penalty: Optional[float] = Field(None, alias="frequency_penalty")
    logit_bias: Optional[Dict[str, int]] = Field(None, alias="logit_bias")
    user: Optional[str] = Field(None, alias="user")

class ChatCompletionChoice(BaseModel):
    index: int
    message: ChatCompletionMessage
    finish_reason: str = Field(..., alias="finish_reason")

class ChatCompletionResponse(BaseModel):
    id: str = Field(..., alias="id")
    object: str = Field(..., alias="object")
    created: int = Field(..., alias="created")
    model: str = Field(..., alias="model")
    choices: List[ChatCompletionChoice]
    usage: Usage
