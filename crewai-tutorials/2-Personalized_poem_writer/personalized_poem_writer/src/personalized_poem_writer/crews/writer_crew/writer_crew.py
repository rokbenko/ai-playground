import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

load_dotenv()


@CrewBase
class WriterCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def senior_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_writer"],
            llm=LLM(
                api_key=os.getenv("MISTRAL_API_KEY"),
                model="mistral/mistral-large-latest",
            ),
            max_iter=1,
            verbose=True,
        )

    @task
    def write_poem(self) -> Task:
        return Task(
            config=self.tasks_config["write_poem"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            output_log_file="logs/writer_crew.json",
            verbose=True,
        )
