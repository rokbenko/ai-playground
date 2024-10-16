import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from podcast_prepper.tools.custom_tool import ExaGuestResearchTool

load_dotenv()


@CrewBase
class GuestResearchCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def senior_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_researcher"],
            llm=LLM(
                api_key=os.getenv("ANTHROPIC_API_KEY"),
                model="anthropic/claude-3-haiku-20240307",
            ),
            respect_context_window=True,
            max_iter=1,
            verbose=True,
            tools=[ExaGuestResearchTool()],
        )

    @agent
    def senior_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_reporter"],
            llm=LLM(
                api_key=os.getenv("ANTHROPIC_API_KEY"),
                model="anthropic/claude-3-haiku-20240307",
            ),
            respect_context_window=True,
            max_iter=1,
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            human_input=True,
        )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            output_log_file="log_guest_research_crew.txt",
            verbose=True,
        )
