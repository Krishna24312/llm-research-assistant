# LLM Research Assistant (CLI)

A small command-line research assistant built using **LangChain** and **OpenAI**.  
It takes a user query, pulls information from **Wikipedia** and **DuckDuckGo**, and compiles a structured summary that can also be saved to a local text file.

I built this mainly to explore **tool-calling agents**, **Pydantic output models**, and how multiple information sources can be combined in a single workflow.

---

## Features

- Uses **GPT-4o-mini** as the main LLM
- Automatically calls two external tools:
  - **Wikipedia** (background knowledge)
  - **DuckDuckGo Search** (recent information)
- Combines both sources into a single **structured response**
- Supports saving results to a local **text file**
- Clean separation of code:
  - `main.py` → agent logic (prompt, parser, execution)
  - `tools.py` → all custom tools (Wikipedia, DuckDuckGo, save-to-file)

---

## Project Structure

AI_Python_Basic/
│
├── main.py # Agent setup, prompt, parser, and execution
├── tools.py # Wikipedia, DuckDuckGo, and save-to-file tools
├── .gitignore
└── README.md

yaml
Copy code

---

## How to Run

### 1) Create and activate environment
```bash
conda create -n llm-agent python=3.11 -y
conda activate llm-agent
2) Install dependencies
bash
Copy code
pip install -r requirements.txt
Make sure your .env file is in the same folder with your API keys.

3) Run the script
bash
Copy code
python main.py
You’ll see:

bash
Copy code
What can I help you search?
Type any research topic and the agent will take over from there.

Environment Variables
Create a .env file in the project directory:

env
Copy code
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=optional
The .env file is ignored by git and won’t be uploaded.

Why I Built This
I wanted a compact project that touches a few modern concepts:

Tool-calling LLM agents

Pydantic-based structured output

Integrating multiple data sources

Clean separation between tools and orchestration logic

Working with LangChain’s newer “classic” agents

It was a good way to understand how LLMs behave when they have access to external knowledge instead of generating everything themselves.

Future Improvements
Some things I plan to add:

Optional web UI using Streamlit

More tools (e.g., arXiv search, YouTube transcripts)

Better output formatting

Caching so repeated queries run faster

pgsql
Copy code

If you want, paste your actual repo name (folder name + file names) and I’ll align the **Project Structure** block exactly to your real layout.