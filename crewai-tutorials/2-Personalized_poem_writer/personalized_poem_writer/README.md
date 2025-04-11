# #2 Personalized poem writer

## 📖 Description 📖

Python example using [CrewAI](https://www.crewai.com/), [Mistral Large 2](https://mistral.ai/news/mistral-large-2407) as an LLM, and [Exa](https://exa.ai/) as a tool.

It's designed for creative writers and lyricists, helping them:

- research a person,
- prepare detailed insights about the person, and
- write a personalized, funny, and light-hearted poem inspired by the person's life story.

👉 Refer to the [`rok_benko_poem.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/outputs/rok_benko_poem.txt) file for an example of the poem if the entered person is _Rok Benko_.

<br>

## 🧐 Problem addressed 🧐

Writing personalized poems can be a time-consuming and challenging task, especially when trying to capture the essence of someone's life story in a creative and engaging way. ChatGPT struggles with this task. I tested it with the web search feature turned on and with me (i.e., _Rok Benko_) passed as the person, and while the poem was impressive, it wasn’t about me at all. It was about Rok Benkovič, the former Slovene ski jumper. I clearly asked for a poem inspired by my life story, but ChatGPT completely missed the point. This happened because it sourced the web about Rok Benkovič, not me. Even more confusing, it showed a screenshot of my coding tutorial as a clickable thumbnail, which had nothing to do with the poem.

![ChatGPT test](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/assets/images/chatgpt_test.png)

<br>

## 🧠 Learning goal 🧠

- **Solving the addressed problem with CrewAI:** We'll demonstrate how the CrewAI framework can drastically reduce the time required to write personalized poems by leveraging a multi-agent AI system. By employing [CrewAI Flows](https://docs.crewai.com/concepts/flows), we cut down the writing time from hours to just ≈4 minutes, achieving a ≈95%+ reduction in time spent, all for ≈$0.27 in total!

> [!NOTE]
> This $0.27 covers all expenses, including both the Mistral LLM and Exa tool. For more details about the cost, refer to the [Behind the scenes](https://github.com/rokbenko/ai-playground/tree/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer#-behind-the-scenes-) section.

<br>

## 🚀 Getting started 🚀

This project requires Python `>=3.10 <3.13` and uv for dependency management. Please install both before proceeding:

- [Download Python](https://www.python.org/downloads/)
- [Install uv](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)

> [!NOTE]
> The instructions are specific to Windows. For macOS or Linux, please use the corresponding commands for your operating system.

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer`
3. Create an `.env` file in the root directory to set up your environment variables (_Note: Refer to the example below for the required environment variables._)
4. Create a virtual environment using uv: `uv venv`
5. Activate the virtual environment using uv: `.venv\scripts\activate`
6. Install the dependencies using uv: `uv pip install .`
7. Run the CrewAI flow: `crewai flow kickoff`

> [!IMPORTANT]
> Your `.env` file should contain the following environment variables:
>
> ```bash
> MISTRAL_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx"
> EXA_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx"
> ```

<br>

## ⚒️ Tech stack ⚒️

The project uses the following main tech stack:

- [Python](https://www.python.org/)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [CrewAI Python SDK](https://pypi.org/project/crewai/)
- [CrewAI Tools Python SDK](https://pypi.org/project/crewai-tools/)
- [Exa Python SDK](https://pypi.org/project/exa-py/)
- [Rich](https://pypi.org/project/rich/)

For more detailed information, please refer to the [`uv.lock`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/uv.lock) file.

<br>

## ⚙️ Workflow ⚙️

1. Run the CrewAI flow: `crewai flow kickoff`
2. Enter the person's first and last name
3. CrewAI working... (_Note: You don't need to do anything._)
4. When the Research crew collects data on the person, it will prompt you for human input (i.e., feedback)
5. CrewAI working... (_Note: You don't need to do anything._)
6. The project's final output is saved in the format `<name>_<surname>_poem.txt` (_Note: For an example, refer to the [`rok_benko_poem.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/outputs/rok_benko_poem.txt) file, generated if the entered person is Rok Benko._)

After running the CrewAI flow, a terminal input prompt will appear, as shown in the screenshot below. Enter the person's first and last name. For example, I entered _Rok Benko_.

![Person input prompt](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/assets/images/person_input_prompt.png)

> [!WARNING]
> After the Research crew collects data on the person, it will prompt you for human input. At this stage, you can make any necessary corrections or simply hit <kbd>Enter</kbd>. **It's crucial to hit <kbd>Enter</kbd> if you're satisfied with gathered data, as the flow will not continue without your confirmation.** You have the flexibility to request an edit, addition, or removal of any data gathered by the crew. The crew will rerun the process, making adjustments based on your feedback.
>
> [CrewAI's human-in-the-loop](https://docs.crewai.com/how-to/human-input-on-execution) integration is particularly useful for the project in the following scenario:
>
> - **Identifying incorrect data:** The Research crew may collect data about a person who shares the same first and last name but is not the person you want the poem for. For instance, the crew might list a social media profile link of someone else with the same name.
>   - Solution: You can provide input like, _Change the X link to https://www.x.com/rokbenko, remove the Facebook link completely as this is not the Rok Benko who I want the poem for, and add his YouTube channel link I found on the web: https://www.youtube.com/@rokbenko_.

> [!NOTE]
> Keep in mind that this project is primarily a _proof-of-concept_. While it works well most of the time, occasional errors may occur, or the CrewAI output may not meet expectations. In such cases, rerunning the flow or using the _human-in-the-loop_ feature more effectively should help resolve the issue.

<br>

## 🎭 Behind the scenes 🎭

### Project

The project was built with [CrewAI Flows](https://docs.crewai.com/concepts/flows) by running `crewai create flow personalized_poem_writer`. Flows simplify CrewAI workflow creation by enabling you to easily chain together multiple crews, manage and share state between different tasks, and implement conditional logic, loops, and branching within your workflows, all while ensuring dynamic and responsive interactions.

It consists of two crews, each designed to handle specific aspects of poem writing:

1. **Research crew**

- Description: The Research crew is responsible for conducting an in-depth investigation into the person. It gathers comprehensive data about the person's background, career milestones, public image, and more, ensuring a well-rounded profile.
- Agents in this crew:
  - Senior Researcher: This agent conducts an in-depth investigation into the person.
- Tasks in this crew:
  - Research: This task involves gathering detailed data about the person, focusing on aspects such as background, education, career milestones, and more. The output is a structured JSON file.
- Tools used by this crew:
  - Exa: This tool searches the web for data about the person.
- Log: You can review an example log from the Research crew, generated when I entered _Rok Benko_ as a person, by checking the [`research_crew.json`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/logs/research_crew.json) file.

2. **Writer crew**

- Description: The Writer crew is responsible for crafting a personalized, funny, and light-hearted poem based on the data collected by the Research crew.
- Agents in this crew:
  - Senior Writer: This agent writes the poem for the person based on the data collected by the Research crew.
- Tasks in this crew:
  - Write Poem: This task involves creating a poem based on the data collected by the Research crew. The output is a text file containing the poem.
- Tools used by this crew: No tools are specified for this crew.
- Log: You can review an example log from the Writer crew, generated when I entered _Rok Benko_ as a person, by checking the [`writer_crew.json`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/logs/writer_crew.json) file.

### Commands

The [`pyproject.toml`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/pyproject.toml) file includes two commands:

- `crewai flow kickoff`, which kickoffs the flow, and
- `crewai flow plot`, which plots the flow.

### Cost

The total cost depends on the flow run, but it's ≈$0.27 when using the [Mistral Large 2](https://mistral.ai/news/mistral-large-2407) LLM. As of writing this, it costs $2 per million input tokens and $6 per million output tokens. See the [Mistral Pricing page](https://mistral.ai/products/la-plateforme#pricing).

Here’s a detailed cost breakdown based on the [`token_usage.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/logs/token_usage.txt) file:

- [Mistral Large 2](https://mistral.ai/news/mistral-large-2407) LLM costs: $0.261702
  - Research crew: $0.255872
    - Prompt tokens used: 111,241 → $0.222482 (`111,241 * (2 / 1,000,000)`)
    - Completion tokens used: 5,565 → $0.03339 (`5,565 * (6 / 1,000,000)`)
  - Writer crew: $0.00583
    - Prompt tokens used: 1,913 → $0.003826 (`1,913 * (2 / 1,000,000)`)
    - Completion tokens used: 334 → $0.002004 (`334 * (6 / 1,000,000)`)
- Exa tool costs (_Note: Retrieved from the terminal output._): $0.013

This brings the total cost to $0.274702. Again, I want to emphasize that the total cost depends on the flow run, but it's ≈$0.27.

> [!TIP]
> I tried using a cheaper, less capable Mistral LLM to lower the cost, but I was often getting errors during the flow run since these models work less effectively with CrewAI ([source](https://github.com/crewAIInc/crewAI/issues/103#issuecomment-1902667402)). Even if a flow was executed successfully, outputs tend to be of lower quality. For this reason, I suggest using one of the top LLMs, like [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet), to ensure both reliability and high-quality outputs.

### Plot

[CrewAI Flows](https://docs.crewai.com/concepts/flows) also enables us to visualize the workflow by [plotting the flow](https://docs.crewai.com/concepts/flows#plot-flows). The command for plotting the flow is `crewai flow plot`. The screenshot below is derived from the [`crewai_flow.html`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/crewai_flow.html) file generated by the command.

> [!TIP]
> For higher quality, click on the image.

![Flow plot](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/assets/images/crewai_flow.png)

<br>

## 📽️ Demonstration 📽️

For demonstration purposes, I ran the project and entered _Rok Benko_ as a person. You can review the outputs in the following files:

- [`research_crew.json`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/logs/research_crew.json) file for the output from the Research crew,
- [`rok_benko_data.json`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/outputs/rok_benko_data.json) file for data gathered by the Research crew,
- [`writer_crew.json`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/logs/writer_crew.json) file for the output from the Writer crew,
- [`token_usage.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/logs/token_usage.txt) file for the token usage, and
- [`rok_benko_poem.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/2-Personalized_poem_writer/personalized_poem_writer/outputs/rok_benko_poem.txt) file for the poem on the person.
