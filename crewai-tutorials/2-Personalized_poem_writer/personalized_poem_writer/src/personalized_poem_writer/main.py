#!/usr/bin/env python
import json
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start
from .crews.research_crew.research_crew import ResearchCrew
from .crews.writer_crew.writer_crew import WriterCrew
from rich.console import Console
from rich.prompt import Prompt

output_formatter = Console()


class PersonalizedPoemWriterState(BaseModel):
    user_input: str = ""
    crewai_output: str = ""
    token_usage: str = ""


class PersonalizedPoemWriterFlow(Flow[PersonalizedPoemWriterState]):
    @start()
    def say_hello(self):
        output_formatter.print(
            "[#66FF66]\n🤖 CrewAI: Hi! Who should I write a poem about? Give me his or her name and surname, and I'll craft something unique and inspired by their story![/#66FF66]"
        )

    @listen(say_hello)
    def get_person_name(self):
        user_input = Prompt.ask("\n🧑 You")

        self.state.user_input = user_input

        if user_input.lower() in ["quit", "exit", "q"]:
            output_formatter.print(
                "\n[#66FF66]🤖 CrewAI: Have a nice day! 👋[/#66FF66]\n"
            )

            raise SystemExit

    @listen(get_person_name)
    def get_data_about_person(self):
        crewai_output = (
            ResearchCrew()
            .crew()
            .kickoff(
                inputs={
                    "person": self.state.user_input,
                }
            )
        )

        self.state.crewai_output = crewai_output.raw
        self.state.token_usage = crewai_output.token_usage

        output_formatter.print(f"[#66FF66]🤖 CrewAI:\n{crewai_output.raw}[/#66FF66]")

    @listen(get_data_about_person)
    def save_data_and_token_usage(self):
        formatted_user_input = self.state.user_input.lower().replace(" ", "_")

        try:
            deserialized_output = json.loads(self.state.crewai_output)
        except json.JSONDecodeError:
            deserialized_output = self.state.crewai_output

            output_formatter.print(
                "[#FF0000]Error: Failed to parse CrewAI output as JSON. ❌[/#FF0000]"
            )

        with open(f"outputs/{formatted_user_input}_data.json", "w") as file:
            json.dump(
                deserialized_output,
                file,
                indent=4,
                ensure_ascii=False,
            )

        output_formatter.print(
            f"[#66FF66]\nData about {self.state.user_input} saved to 'outputs/{formatted_user_input}_data.json' file! 🚀\n[/#66FF66]"
        )

        token_usage_string = str(self.state.token_usage)

        with open("logs/token_usage.txt", "w") as file:
            file.write("Person research crew:\n\n")
            file.write(token_usage_string)

        output_formatter.print(
            "[#66FF66]\nToken usage saved to 'logs/token_usage.txt' file! 🚀\n[/#66FF66]"
        )

    @listen(get_data_about_person)
    def write_poem_for_person(self):
        crewai_output = (
            WriterCrew()
            .crew()
            .kickoff(
                inputs={
                    "person": self.state.user_input,
                    "data": self.state.crewai_output,
                }
            )
        )

        self.state.crewai_output = crewai_output.raw
        self.state.token_usage = crewai_output.token_usage

        output_formatter.print(f"[#66FF66]🤖 CrewAI:\n{crewai_output.raw}[/#66FF66]")

    @listen(write_poem_for_person)
    def save_poem_and_token_usage(self):
        formatted_user_input = self.state.user_input.lower().replace(" ", "_")

        with open(f"outputs/{formatted_user_input}_poem.txt", "w") as file:
            file.write(self.state.crewai_output)

        output_formatter.print(
            f"[#66FF66]\nPoem for {self.state.user_input} saved to 'outputs/{formatted_user_input}_poem.txt' file! 🚀\n[/#66FF66]"
        )

        token_usage_string = str(self.state.token_usage)

        with open("logs/token_usage.txt", "a") as file:
            file.write("\n\nPoem writer crew:\n\n")
            file.write(token_usage_string)

        output_formatter.print(
            "[#66FF66]\nToken usage saved to 'logs/token_usage.txt' file! 🚀\n[/#66FF66]"
        )

    @listen(write_poem_for_person)
    def say_goodbye(self):
        output_formatter.print(
            f"[#66FF66]\n🤖 CrewAI: The poem for {self.state.user_input} has been successfully written and saved! 🎉[/#66FF66]\n"
        )


def kickoff():
    personalized_poem_writer_flow = PersonalizedPoemWriterFlow()
    personalized_poem_writer_flow.kickoff()


def plot():
    personalized_poem_writer_flow = PersonalizedPoemWriterFlow()
    personalized_poem_writer_flow.plot()


if __name__ == "__main__":
    kickoff()
