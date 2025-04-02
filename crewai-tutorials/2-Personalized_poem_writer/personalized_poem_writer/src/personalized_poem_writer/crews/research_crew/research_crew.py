import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field, HttpUrl
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from personalized_poem_writer.tools.custom_tool import ExaPersonResearchTool

load_dotenv()


class ResearchCrewOutput(BaseModel):
    person: str = Field(
        ...,
        description="Name and surname of the person being researched.",
    )
    background: str = Field(
        ...,
        description="Background information about the person.",
    )
    education: str = Field(
        ...,
        description="Educational background and qualifications of the person.",
    )
    career: str = Field(
        ...,
        description="Important milestones in the career of the person.",
    )
    publications_and_works: str = Field(
        ...,
        description="Publications and works by the person.",
    )
    awards_and_honors: str = Field(
        ...,
        description="Awards and honors received by the person.",
    )
    current_projects: str = Field(
        ...,
        description="Current projects and initiatives of the person.",
    )
    public_image: str = Field(
        ...,
        description="Public image and reputation of the person.",
    )
    notable_achievements: str = Field(
        ...,
        description="Notable achievements and accomplishments of the person.",
    )
    personal_life: str = Field(
        ...,
        description="Personal life and activities of the person.",
    )
    influence_and_impact: str = Field(
        ...,
        description="Influence and impact of the person on society.",
    )
    challenges_and_controversies: str = Field(
        ...,
        description="Challenges and controversies associated with the person.",
    )
    philanthropy_and_activism: str = Field(
        ...,
        description="Philanthropy and activism of the person.",
    )
    sources: list[HttpUrl] = Field(
        ...,
        description="Full URLs of the sources used to get information about the person.",
    )

    model_config = {"json_encoders": {HttpUrl: str}}

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)

        if "sources" in data:
            data["sources"] = [str(url) for url in data["sources"]]
        return data


@CrewBase
class ResearchCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def senior_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_researcher"],
            llm=LLM(
                api_key=os.getenv("MISTRAL_API_KEY"),
                model="mistral/mistral-large-latest",
            ),
            max_iter=1,
            tools=[ExaPersonResearchTool()],
            verbose=True,
        )

    @task
    def research_person(self) -> Task:
        return Task(
            config=self.tasks_config["research_person"],
            expected_output="The output should be an instance of the Pydantic model class `ResearchCrewOutput`.",
            output_pydantic=ResearchCrewOutput,
            human_input=True,
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            output_log_file="logs/research_crew.json",
            verbose=True,
        )
