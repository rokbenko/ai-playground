import os
from dotenv import load_dotenv
from crewai_tools import BaseTool
from exa_py import Exa

load_dotenv()


class ExaGuestResearchTool(BaseTool):
    name: str = "Exa Guest Research"
    description: str = (
        "Search the web for information about the given guest to create a report"
    )

    def _run(self, guest: str) -> str:
        exa_tool = Exa(api_key=os.getenv("EXA_API_KEY"))

        response = exa_tool.search_and_contents(
            query=guest,
            type="keyword",
            use_autoprompt=False,
            num_results=10,
            text={"max_characters": 3000},
            summary=False,
            livecrawl="always",
        )

        return response


class ExaQuestionsResearchTool(BaseTool):
    name: str = "Exa Questions Research"
    description: str = (
        "Search the web for information based on the guest's report to create questions for the guest"
    )

    def _run(self, topics: str) -> str:
        exa_tool = Exa(api_key=os.getenv("EXA_API_KEY"))

        response = exa_tool.search_and_contents(
            query=topics,
            type="auto",
            use_autoprompt=True,
            num_results=50,
            text={"max_characters": 1000},
            summary=True,
        )

        return response
