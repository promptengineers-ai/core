from typing import Optional, Any
from pydantic import BaseModel, Field

class Retrieval(BaseModel):
    """Contains the information needed to document retrieval augmented generation."""

    provider: Optional[str] = Field(default="pinecone")
    index_name: Optional[str] = None
    search_type: str = Field(default="similarity")
    search_kwargs: Any = None

    __config__ = {
		"json_schema_extra": {
            "example": {
                "provider": "pinecone",
                "index_name": "Formio",
                "search_type": "similarity",
                "search_kwargs": {"k": 5},
            }
        }
    }