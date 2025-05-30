# #1 Podcast prepper

## 📖 Description 📖

Python example using [CrewAI](https://www.crewai.com/), [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) as an LLM, and [Exa](https://exa.ai/) as a tool.

It's designed for podcast hosts, helping them:

- research a guest,
- prepare detailed insights about the guest, and
- suggest relevant questions for an upcoming episode with the guest.

👉 Refer to the [`rok_benko_report.md`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/rok_benko_report.md) file for an example of the final report if the entered guest is _Rok Benko_.

<br>

## 🧐 Problem addressed 🧐

The screenshot below shows [Google Trends](https://trends.google.com/trends/explore?date=all_2008&gprop=youtube&q=podcast&hl=en-US) data for the search term _podcast_ on YouTube worldwide from 2008 to the present, highlighting a clear long-term upward trend in podcast popularity.

![Google Trends data for the search term "podcast" on YouTube from 2008 to the present](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/assets/images/google_trends_podcast_on_youtube.png)

But according to the [Reddit thread](https://www.reddit.com/r/podcasting/comments/18a3f26/how_do_you_prepare_for_interviewing_guests_how/), preparing for a podcast can take several hours!

Nice_Butterscotch995 saying:

> **I would say the prep work averaged three to four hours per episode or thereabouts, longer if they were an author or filmmaker.** At the same time, I would harvest links and photos for my show notes. I wouldn't call the process annoying, but it was definitely a time suck.

Fuzzy_Mic_2021 saying:

> My opinion is that there is no such thing as too much prep. **For a 10 minute interview, I'll do 4 hours of research.** I love the process.

<br>

## 🧠 Learning goal 🧠

- **Solving the addressed problem with CrewAI:** We'll demonstrate how the CrewAI framework can drastically reduce the time required for podcast preparation by leveraging a multi-agent AI system. By employing [CrewAI Flows](https://docs.crewai.com/concepts/flows), we cut down the preparation time from 4 hours to just ≈3 minutes, achieving a 98.75% reduction in time spent, all for ≈$0.13 in total!

> [!NOTE]
> This $0.13 covers all expenses, including both the Anthropic LLM and Exa tool. For more details about the cost, refer to the [Behind the scenes](https://github.com/rokbenko/ai-playground/tree/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper#-behind-the-scenes-) section.

<br>

## 🚀 Getting started 🚀

This project requires Python `>=3.10 <=3.13` and Poetry for dependency management. Please install both before proceeding:

- [Download Python](https://www.python.org/downloads/)
- [Install Poetry](https://python-poetry.org/docs/#installation)

> [!NOTE]
> The instructions are specific to Windows. For macOS or Linux, please use the corresponding commands for your operating system.

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/crewai-tutorials/1-Podcast_prepper/podcast_prepper`
3. Create an `.env` file in the root directory to set up your environment variables (_Note: Refer to the example below for the required environment variables._)
4. Install the dependencies using Poetry: `poetry install` (_Note: This may take a few minutes. Be patient!_)
5. Activate the virtual environment using Poetry: `poetry shell`
6. Run the CrewAI flow using Poetry: `poetry run flow`

> [!IMPORTANT]
> Your `.env` file should contain the following environment variables:
>
> ```bash
> ANTHROPIC_API_KEY = "sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxx"
> EXA_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx"
> ```

<br>

## ⚒️ Tech stack ⚒️

The project uses the following main tech stack:

- [Python](https://www.python.org/)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Asyncio](https://pypi.org/project/asyncio/)
- [CrewAI Python SDK](https://pypi.org/project/crewai/)
- [CrewAI Tools Python SDK](https://pypi.org/project/crewai-tools/)
- [Exa Python SDK](https://pypi.org/project/exa-py/)
- [Rich](https://pypi.org/project/rich/)

For more detailed information, please refer to the [`poetry.lock`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/poetry.lock) file.

<br>

## ⚙️ Workflow ⚙️

1. Run the CrewAI flow using Poetry: `poetry run flow`
2. Enter the guest's first and last name
3. CrewAI working... (_Note: You don't need to do anything._)
4. When the Guest Research crew collects data on the guest, it will prompt you for human input (i.e., feedback)
5. CrewAI working... (_Note: You don't need to do anything._)
6. The project's final output is saved in the format `<name>_<surname>_report.md` (_Note: For an example, refer to the [`rok_benko_report.md`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/rok_benko_report.md) file, generated if the entered guest is Rok Benko._)

After running the CrewAI flow, a terminal input prompt will appear, as shown in the screenshot below. Enter the guest's first and last name. For example, I entered _Rok Benko_.

![Guest input prompt](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/assets/images/guest_input_prompt.png)

> [!WARNING]
> After the Guest Research crew collects data on the guest, it will prompt you for human input. At this stage, you can make any necessary corrections or simply respond with something like _Everything is fine, continue_. **It's crucial to provide feedback, even if you're satisfied with gathered data, as the flow will not continue without your confirmation.** You have the flexibility to request an edit, addition, or removal of any data gathered by the crew. The crew will rerun the process, making adjustments based on your feedback.
>
> [CrewAI's human-in-the-loop](https://docs.crewai.com/how-to/human-input-on-execution) integration is particularly useful for the project in the following scenarios:
>
> - **Identifying incorrect data:** The Guest Research crew may collect data about a person who shares the same first and last name but is not your guest. For instance, the crew might list a social media profile link of someone else with the same name.
>   - Solution: You can provide input like, _Change the X link to https://www.x.com/rokbenko, remove the Facebook link completely as this is not the Rok Benko who will be my guest, and add his YouTube channel link I found on the web: https://www.youtube.com/@rokbenko_.
> - **Requesting a full report:** The Guest Research crew may occasionally return a short summary instead of a complete markdown report on the guest.
>   - Solution: Simply respond with, _Write a full markdown report_.

> [!IMPORTANT]
> Don't use phrases like _My guest is \<Name> \<Surname>_. This will not generate the expected report due to the configuration of the Exa web search tool. Only enter the guest's first and last name.
>
> ✔️ _\<Name> \<Surname>_<br>
> ❌ _Guest: \<Name> \<Surname>_<br>
> ❌ _I will guest \<Name> \<Surname>_<br>
> ❌ _My guest is \<Name> \<Surname>_

> [!NOTE]
> Keep in mind that this project is primarily a _proof-of-concept_. While it works well most of the time, occasional errors may occur, or the CrewAI output may not meet expectations. In such cases, rerunning the flow or using the _human-in-the-loop_ feature more effectively should help resolve the issue.

<br>

## 🎭 Behind the scenes 🎭

### Project

The project was built with [CrewAI Flows](https://docs.crewai.com/concepts/flows) by running `crewai create flow podcast_prepper`. Flows simplify CrewAI workflow creation by enabling you to easily chain together multiple crews, manage and share state between different tasks, and implement conditional logic, loops, and branching within your workflows, all while ensuring dynamic and responsive interactions.

It consists of two crews, each designed to handle specific aspects of podcast preparation:

1. **Guest Research crew**

- Description: The Guest Research crew is responsible for conducting an in-depth investigation into the podcast guest. It gathers comprehensive data about the guest's background, career milestones, public image, and more, ensuring a well-rounded profile.
- Agents in this crew:
  - Senior Researcher: This agent conducts an in-depth investigation into the podcast guest.
- Tasks in this crew:
  - Research: This task involves gathering detailed data about the guest, focusing on aspects such as background, education, career milestones, and more. The output is a structured markdown report.
- Tools used by this crew:
  - Exa: This tool searches the web for data about the guest.
- Log: You can review an example log from the Guest Research crew, generated when I entered _Rok Benko_ as a guest, by checking the [`log_guest_research_crew.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_guest_research_crew.txt) file.

2. **Questions Research crew**

- Description: The Questions Research crew is responsible for formulating a set of relevant and thought-provoking questions for the guest based on the data collected by the Guest Research crew. It ensures the questions are designed to be engaging and encourage a personal dialogue, often exploring philosophical themes.
- Agents in this crew:
  - Senior Journalist: This agent creates insightful questions for the podcast guest based on the collected data by the Guest Research crew.
- Tasks in this crew:
  - Journalism: This task involves forming relevant and thought-provoking questions for the guest based on the data collected by the Guest Research crew. The output is a markdown list of questions, phrased in the first person and structured chronologically.
- Tools used by this crew: No tools are specified for this crew.
- Log: You can review an example log from the Questions Research crew, generated when I entered _Rok Benko_ as a guest, by checking the [`log_questions_research_crew.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_questions_research_crew.txt) file.

### Commands

The [`pyproject.toml`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/pyproject.toml) file includes two commands:

- `poetry run flow`, which kickoffs the flow, and
- `poetry run plot`, which plots the flow.

### Cost

The total cost depends on the flow run, but it's ≈$0.13 when using the [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) LLM. As of writing this, it costs $3 per million input tokens and $15 per million output tokens. See the [Anthropic Pricing page](https://www.anthropic.com/pricing#anthropic-api). Even if the total cost reaches $0.14 or $0.15, consider the value of your time. Would you trade $0.15 for 4 hours of manual work?

Here’s a detailed cost breakdown based on the [`log_token_usage.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_token_usage.txt) file:

- [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) LLM costs: $0.121734
  - Guest Research crew: $0.096675
    - Prompt tokens used: 14,410 → $0.04323 (`14,410 * (3 / 1,000,000)`)
    - Completion tokens used: 3,563 → $0.053445 (`3,563 * (15 / 1,000,000)`)
  - Questions Research crew: $0.025059
    - Prompt tokens used: 3,908 → $0.011724 (`3,908 * (3 / 1,000,000)`)
    - Completion tokens used: 889 → $0.013335 (`889 * (15 / 1,000,000)`)
- Exa tool costs (_Note: Estimated, refer to the note below._): $0.015

This brings the total cost to $0.136734. Again, I want to emphasize that the total cost depends on the flow run, but it's ≈$0.13.

> [!TIP]
> I tried using a cheaper, less capable Anthropic LLM to lower the cost, but I was often getting errors during the flow run since these models work less effectively with CrewAI ([source](https://github.com/crewAIInc/crewAI/issues/103#issuecomment-1902667402)). Even if a flow was executed successfully, outputs tend to be of lower quality. For this reason, I suggest using one of the top LLMs, like [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet), to ensure both reliability and high-quality outputs.

> [!NOTE]
> Currently, the Exa dashboard doesn't provide visibility into the exact cost per run. However, these expenses are generally small. Over many runs building this project, I spent only $0.65 on Exa. Estimating the cost per run at $0.015 is likely a reasonable approximation.

### Plot

[CrewAI Flows](https://docs.crewai.com/concepts/flows) also enables us to visualize the workflow by [plotting the flow](https://docs.crewai.com/concepts/flows#plot-flows). I configured the command for plotting the flow as `poetry run plot`. The screenshot below is derived from the [`crewai_flow.html`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/crewai_flow.html) file generated by the command.

> [!TIP]
> For higher quality, click on the image.

![Flow plot](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/assets/images/crewai_flow.png)

<br>

## 📽️ Demonstration 📽️

For demonstration purposes, I ran the project and entered _Rok Benko_ as a guest. You can review the outputs in the following files:

- [`log_guest_research_crew.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_guest_research_crew.txt) file for the output from the Guest Research crew,
- [`log_questions_research_crew.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_questions_research_crew.txt) file for the output from the Questions Research crew,
- [`log_token_usage.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_token_usage.txt) file for the token usage, and
- [`rok_benko_report.md`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/rok_benko_report.md) file for the final report on the guest.
