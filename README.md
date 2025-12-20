# LLM Research Assistant (CLI)

A small command-line research assistant built using **LangChain** and **OpenAI**.  
It takes a user query, pulls information from **Wikipedia** and **DuckDuckGo**, and compiles a structured summary that can also be saved to a local text file.

I built this mainly to explore **tool-calling agents**, **Pydantic output models**, and how multiple information sources can be combined inside a single workflow.

---

## Features

- Uses **GPT-4o-mini** as the main LLM
- Automatically calls two external tools:
  - **Wikipedia** (background knowledge)
  - **DuckDuckGo Search** (recent information)
- Combines both sources into a single **structured response**
- Supports saving results to a local text file
- Clean separation:
  - `main.py` → agent logic (prompt, parser, orchestration)
  - `tools.py` → Wikipedia, DuckDuckGo, and save-to-file tools
- `demo.py` included for quick experimentation / reference (Pydantic usage notes)

---

## Project Structure

llm-research-assistant/
├── .gitignore
├── README.md
├── demo.py
├── main.py
├── req.txt
├── research_output.txt
└── tools.py

yaml
Copy code

---

## Setup

### 1) Create and activate environment (Conda)
```bash
conda create -n llm-agent python=3.11 -y
conda activate llm-agent
2) Install dependencies
Your repo uses req.txt:

bash
Copy code
pip install -r req.txt
3) Add API key (recommended)
Create a .env file in the project folder (same level as main.py):

env
Copy code
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=optional
The .env file is ignored by git and won’t be uploaded.

Run
bash
Copy code
python main.py
You’ll see something like:

bash
Copy code
What can I help you search?
Type any research topic and the agent will take over from there.

Output
The assistant prints a structured response in the terminal.

If saving is enabled in your workflow/tools, the output can be written to:

research_output.txt

Why I Built This
I wanted a compact project that touches a few modern concepts:

Tool-calling LLM agents

Pydantic-based structured output

Integrating multiple data sources

Clean separation between tools and orchestration logic

Understanding how LLMs behave with external knowledge sources instead of generating everything from scratch