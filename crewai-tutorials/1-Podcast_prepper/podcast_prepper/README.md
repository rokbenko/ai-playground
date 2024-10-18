# #1 Podcast prepper

<br>

## 📖 Description 📖

Python example using [CrewAI](https://www.crewai.com/), [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) as an	LLM, and [Exa](https://exa.ai/) as a tool.

It's designed for podcast hosts, helping them:
 - research a guest,
 - prepare detailed insights about the guest, and
 - suggest relevant questions for an upcoming episode with the guest.

<br>

## 🧐 Problem addressed 🧐

The screenshot below shows [Google Trends](https://trends.google.com/trends/explore?date=all_2008&gprop=youtube&q=podcast&hl=en-US) data for the search term *podcast* on YouTube worldwide from 2008 to the present, highlighting a clear long-term upward trend in podcast popularity.

![Google Trends data for the search term "podcast" on YouTube from 2008 to the present](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/google_trends_podcast_on_youtube.png)

But according to the [Reddit thread](https://www.reddit.com/r/podcasting/comments/18a3f26/how_do_you_prepare_for_interviewing_guests_how/), preparing for a podcast can take several hours!

Nice_Butterscotch995 saying:

> **I would say the prep work averaged three to four hours per episode or thereabouts, longer if they were an author or filmmaker.** At the same time, I would harvest links and photos for my show notes. I wouldn't call the process annoying, but it was definitely a time suck.

Fuzzy_Mic_2021 saying:

> My opinion is that there is no such thing as too much prep. **For a 10 minute interview, I'll do 4 hours of research.** I love the process.

<br>

## 🧠 Learning goal 🧠

- **Solving the addressed problem with CrewAI:** We'll demonstrate how the CrewAI framework can drastically reduce the time required for podcast preparation by leveraging a multi-agent AI system. By employing [CrewAI Flows](https://docs.crewai.com/concepts/flows), we cut down the preparation time from 4 hours to just 1 minute, achieving a 99% reduction in time spent, all for approximately $0.12!

> [!NOTE]
> The cost depends on the flow run, but it typically ranges between $0.11 and $0.13 when using [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) LLM. Even if it reaches $0.15, consider the value of your time. Would you trade $0.15 for 4 hours of manual work?
>
> I tested using a cheaper, less capable LLM, but errors can occur since these models work less effectively with CrewAI ([source](https://github.com/crewAIInc/crewAI/issues/103#issuecomment-1902667402)). Even if no errors happen, the final report tends to be of much lower quality. For this reason, I suggest using one of the top LLMs, like [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet), to ensure both reliability and high-quality output.

<br>

## 🚀 Installation 🚀

> [!NOTE]
> The instructions are specific to Windows. For macOS or Linux, please use the corresponding commands for your operating system.

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/crewai-tutorials/1-Podcast_prepper/podcast_prepper`
3. Create an `.env` file in the root directory to set up your environment variables (*Note: See which ones below.*)
4. Install the dependencies using Poetry: `poetry install` (*Note: This may take a few minutes. Be patient!*)
5. Activate the virtual environment using Poetry: `poetry shell`
6. Run the CrewAI flow using Poetry: `poetry run start`

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
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [Asyncio](https://pypi.org/project/asyncio/)
- [CrewAI Python SDK](https://pypi.org/project/crewai/)
- [CrewAI Tools Python SDK](https://pypi.org/project/crewai-tools/)
- [Exa Python SDK](https://pypi.org/project/exa-py/)

For more detailed information, please refer to the [`poetry.lock`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/poetry.lock) file.

<br>

## ⚙️ Workflow ⚙️

1. Run the CrewAI flow: `poetry run start`
2. Enter the guest's first and last name
3. CrewAI working... (*Note: You don't need to do anything.*)
4. When the Guest Research crew collects data on the guest, it will prompt you for human input (i.e., feedback)
5. CrewAI working... (*Note: You don't need to do anything.*)
6. The project's final output is saved in the format `<name>_<surname>_report.md` (*Note: For an example, refer to the [`rok_benko_report.md`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/rok_benko_report.md) file, generated when I entered *Rok Benko* as a guest.*)

After starting the CrewAI flow, a terminal input prompt will appear, as shown in the screenshot below. Enter the guest's first and last name. For example, I entered *Rok Benko*.

![Guest input prompt](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/guest_input_prompt.png)

> [!WARNING]
> After the Guest Research crew collects data on the guest, it will prompt you for human input. At this stage, you can make any necessary corrections or simply respond with something like *Everything is fine, continue*. **It's crucial to provide input, even if you're satisfied with the report, as the flow will not continue without your confirmation.** You have the flexibility to edit, add, or request the deletion of any information gathered by the crew. Additionally, you can specify what you don't like in the report, and the crew will rerun the process, making adjustments to improve the report based on your feedback.
>
>  [CrewAI's human-in-the-loop](https://docs.crewai.com/how-to/human-input-on-execution) integration is particularly useful for the project in the following scenarios:
>
> - **Identifying incorrect data:** The Guest Research crew may collect data about a person who shares the same first and last name but is not your guest. For instance, the crew might list a social media profile link for someone else with the same name.
>   - Solution: You can provide input like, *Change the Twitter link to https://www.x.com/rokbenko, remove the Facebook link completely as this is not the Rok Benko who will be my guest, and add his YouTube channel link I found online: https://www.youtube.com/@rokbenko*.
> - **Requesting a full report:** The Guest Research crew may occasionally return a short summary instead of a complete markdown report on the guest.
>   - Solution: Simply respond with, *Write a full markdown report*.

> [!IMPORTANT]
> Don't use phrases like *My guest is \<Name> \<Surname>*. This will not generate the expected report due to the configuration of the Exa web search tool. Only enter the guest's first and last name.
>
> ✔️ *\<Name> \<Surname>*<br>
> ❌ *Guest: \<Name> \<Surname>*<br>
> ❌ *I will guest \<Name> \<Surname>*<br>
> ❌ *My guest is \<Name> \<Surname>*

> [!NOTE]
> Keep in mind that this project is primarily a *proof-of-concept*. While it works well most of the time, occasional errors may occur, or the CrewAI output may not meet expectations. In such cases, rerunning the flow or using the *human-in-the-loop* feature more effectively should help resolve the issue.

<br>

## 🎭 Behind the sceenes 🎭

The project was built with [CrewAI Flows](https://docs.crewai.com/concepts/flows) by running `crewai create flow podcast_prepper`. Flows simplify CrewAI workflow creation by enabling you to easily chain together multiple crews, manage and share state between different tasks, and implement conditional logic, loops, and branching within your workflows, all while ensuring dynamic and responsive interactions.

It consists of three main crews, each designed to handle specific aspects of podcast preparation:

1. **Guest Research crew**
- Description: The Guest Research crew is responsible for conducting an in-depth investigation into the podcast guest. It gathers comprehensive information about the guest's background, career milestones, public image, and more, ensuring a well-rounded profile.
- Agents in this crew:
  - Senior Researcher: This agent conducts an in-depth investigation into the podcast guest.
- Tasks in this crew:
  - Research: This task involves gathering detailed information about the guest, focusing on aspects such as background, education, career milestones, and more. The output is a structured markdown report.
- Tools used by this crew:
  - Exa: This tool searches the web for information about the guest.
- Log: You can review an example log from the Guest Research crew, generated when I entered *Rok Benko* as a guest, by checking the [`log_guest_research_crew.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_guest_research_crew.txt) file.

2. **Questions Research crew**
- Description: The Questions Research crew is responsible for formulating a set of relevant and thought-provoking questions for the guest. It ensures the questions are designed to be engaging and encourage a personal dialogue, often exploring philosophical themes.
- Agents in this crew:
  - Senior Journalist: This agent creates insightful questions for the podcast guest.
- Tasks in this crew:
  - Journalism: This task involves forming questions based on the guest's report made by the previous crew. The output is a markdown list of questions, phrased in the first person and structured chronologically.
- Tools used by this crew: No tools are specified for this crew.
- Log: You can review an example log from the Questions Research crew, generated when I entered *Rok Benko*, by checking the [`log_questions_research_crew.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_questions_research_crew.txt) file.

3. **Cost Calculation crew**
- Description: The Cost Calculation crew is responsible for calculating the cost of the current flow run based on token usage. It provides a detailed report of the costs.
- Agents in this crew:
  - Senior Mathematician: This agent calculates costs and is proficient in Python for performing calculations.
- Tasks in this crew:
  - Cost Calculation: This task involves calculating the cost of CrewAI usage by analyzing token usage data. The output is a markdown report detailing the costs for each crew and the total cost, including the Python code used for calculations.
- Tools used by this crew: No tools are specified for this crew. However, the Senior Mathematician agent has set the `allow_code_execution parameter` to `True`, which enables the agent to use CrewAI's internal code execution tool (i.e., [CodeInterpreterTool](https://docs.crewai.com/tools/codeinterpretertool)).
- Log: You can review an example log from the Cost Calculation crew, generated when I entered *Rok Benko*, by checking the [`log_cost_calculation_crew.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_cost_calculation_crew.txt) file.

> [!NOTE]
> The calculated cost by the Cost Calculation crew is just an estimate because:
>  - The Cost Calculation crew itself also uses some tokens that are not reflected in the calculation.
>  - The Exa tool incurs costs that are not reflected in the calculation.
> 
> The Cost Calculation crew's costs are excluded because the exact number of tokens used by this crew is only available after execution. However, the token usage of the Cost Calculation crew is expected to be approximately $0.03 when using [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) LLM. To get the complete total, you can manually calculate and add the Cost Calculation crew's cost to the Total Cost calculated in the [`rok_benko_report.md`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/rok_benko_report.md) file. To manually calculate the cost of the Cost Calculation crew, refer to the Cost Calculation Crew section in the [`log_token_usage.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_token_usage.txt) file, then manually calculate the cost for prompt and completion tokens. All agents utilize the [Anthropic Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) LLM, which incurs a charge of $3 per million input (i.e., prompt) tokens and $15 per million output (i.e., completion) tokens. See the [Anthropic Pricing page](https://www.anthropic.com/pricing#anthropic-api).
>
> The Exa tool costs are excluded because the Exa dashboard currently does not provide visibility into the exact costs per run. However, the expenses should not be huge. Overall, I spent $0.65 on Exa during my numerous(!) flow runs while working on this project.

CrewAI Flows also enables us to visualize the workflow. I configured the command for plotting the flow as `poetry run plot`. The screenshot below is derived from the [`crewai_flow.html`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/crewai_flow.html) file generated by the CrewAI CLI.

> [!TIP]
> For higher quality, please click on the image.

![Flow plot](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/crewai_flow.png)

<br>

## 📽️ Demonstration 📽️

For demonstration purposes, I ran the project and entered *Rok Benko* as a guest. You can review the outputs from the following files:
- [`log_guest_research_crew.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_guest_research_crew.txt) file for the output from the Guest Research crew,
- [`log_questions_research_crew.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_questions_research_crew.txt) file for the output from the Questions Research crew,
- [`log_cost_calculation_crew.txt`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/log_cost_calculation_crew.txt) file for the output from the Cost Calculation crew, and
- [`rok_benko_report.md`](https://github.com/rokbenko/ai-playground/blob/main/crewai-tutorials/1-Podcast_prepper/podcast_prepper/rok_benko_report.md) file for the final report.
