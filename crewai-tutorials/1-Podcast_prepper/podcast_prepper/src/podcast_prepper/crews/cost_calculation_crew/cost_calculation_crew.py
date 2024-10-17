import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

load_dotenv()


@CrewBase
class CostCalculationCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def senior_mathematician(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_mathematician"],
            llm=LLM(
                api_key=os.getenv("ANTHROPIC_API_KEY"),
                model="anthropic/claude-3-5-sonnet-20240620",
            ),
            respect_context_window=True,
            max_iter=1,
            verbose=True,
            allow_code_execution=True,
        )

    @task
    def cost_calculation_task(self) -> Task:
        return Task(
            config=self.tasks_config["cost_calculation_task"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            output_log_file="log_cost_calculation_crew.txt",
            verbose=True,
        )
