from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field

from .common import Usage

class EmbeddingModel(str, Enum):
    Unknown = 'unknown'
    AdaSimilarity = 'text-similarity-ada-001'
    BabbageSimilarity = 'text-similarity-babbage-001'
    CurieSimilarity = 'text-similarity-curie-001'
    DavinciSimilarity = 'text-similarity-davinci-001'
    AdaSearchDocument = 'text-search-ada-doc-001'
    AdaSearchQuery = 'text-search-ada-query-001'
    BabbageSearchDocument = 'text-search-babbage-doc-001'
    BabbageSearchQuery = 'text-search-babbage-query-001'
    CurieSearchDocument = 'text-search-curie-doc-001'
    CurieSearchQuery = 'text-search-curie-query-001'
    DavinciSearchDocument = 'text-search-davinci-doc-001'
    DavinciSearchQuery = 'text-search-davinci-query-001'
    AdaCodeSearchCode = 'code-search-ada-code-001'
    AdaCodeSearchText = 'code-search-ada-text-001'
    BabbageCodeSearchCode = 'code-search-babbage-code-001'
    BabbageCodeSearchText = 'code-search-babbage-text-001'
    AdaEmbeddingV2 = 'text-embedding-ada-002'


class Embedding(BaseModel):
    object: str = Field(..., alias="object")
    embedding: List[float]
    index: int


class EmbeddingResponse(BaseModel):
    object: str = Field(..., alias="object")
    data: List[Embedding]
    model: EmbeddingModel
    usage: Usage


class EmbeddingRequest(BaseModel):
    input: List[str] = Field(..., alias="input")
    model: EmbeddingModel
    user: Optional[str]  # optional field
