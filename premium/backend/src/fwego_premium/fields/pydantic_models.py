from langchain_core.pydantic_v1 import BaseModel, Field


class FwegoFormulaModel(BaseModel):
    formula: str = Field(description="The generated Fwego formula")
