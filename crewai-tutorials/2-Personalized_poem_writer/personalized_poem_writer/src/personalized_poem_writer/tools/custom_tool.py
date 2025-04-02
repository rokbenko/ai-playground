import os
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from exa_py import Exa


class ExaPersonResearchToolInput(BaseModel):
    """Input schema for ExaPersonResearchTool."""

    web_search_query: str = Field(
        ..., description="Query to search the web for information."
    )


class ExaPersonResearchTool(BaseTool):
    name: str = "Exa Person Research"
    description: str = "Search the web for information about the given person."
    args_schema: Type[BaseModel] = ExaPersonResearchToolInput

    def _run(self, web_search_query: str) -> str:
        exa_tool = Exa(api_key=os.getenv("EXA_API_KEY"))

        response = exa_tool.search_and_contents(
            query=web_search_query,
            use_autoprompt=True,
            num_results=10,
            livecrawl="always",
            summary=False,
            text={"max_characters": 5000},
        )

        return response
