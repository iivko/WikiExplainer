from typing import List, Dict, Any

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class SummaryText(BaseModel):
    text: str = Field(description="summary")
    facts: List[str] = Field(description="Interesting facts about them")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "text": self.text,
            "facts": self.facts
        }


text_parser = PydanticOutputParser(pydantic_object=SummaryText)