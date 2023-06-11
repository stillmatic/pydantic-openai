"""Moderation endpoint.

Reference: https://platform.openai.com/docs/api-reference/moderations/create
"""
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field

class ModerationModel(str, Enum):
    ModerationTextStable = "text-moderation-stable"
    ModerationTextLatest = "text-moderation-latest"
    ModerationText001    = "text-moderation-001"


class ModerationRequest(BaseModel):
    input: Optional[str] = Field(None, alias="input")
    model: Optional[ModerationModel] = Field(None, alias="model")


class ResultCategories(BaseModel):
    hate: bool = Field(..., alias="hate")
    hate_threatening: bool = Field(..., alias="hate/threatening")
    self_harm: bool = Field(..., alias="self-harm")
    sexual: bool = Field(..., alias="sexual")
    sexual_minors: bool = Field(..., alias="sexual/minors")
    violence: bool = Field(..., alias="violence")
    violence_graphic: bool = Field(..., alias="violence/graphic")


class ResultCategoryScores(BaseModel):
    hate: float = Field(..., alias="hate")
    hate_threatening: float = Field(..., alias="hate/threatening")
    self_harm: float = Field(..., alias="self-harm")
    sexual: float = Field(..., alias="sexual")
    sexual_minors: float = Field(..., alias="sexual/minors")
    violence: float = Field(..., alias="violence")
    violence_graphic: float = Field(..., alias="violence/graphic")


class Result(BaseModel):
    categories: ResultCategories = Field(..., alias="categories")
    category_scores: ResultCategoryScores = Field(..., alias="category_scores")
    flagged: bool = Field(..., alias="flagged")


class ModerationResponse(BaseModel):
    id: str = Field(..., alias="id")
    model: ModerationModel = Field(..., alias="model")
    results: List[Result] = Field(..., alias="results")
