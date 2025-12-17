from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent

from tools import search_tool, wiki_tool, save_tool


# ------------------ Setup ------------------ #

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


# LLM (OpenAI)
llm = ChatOpenAI(model="gpt-4o-mini")

# Structured output parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Prompt for the agent
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools. Give the answer in 500–1000 words.

            For every user query:
            1. First, use the wikipedia tool to get a solid background summary.
            2. Then, use the web-search tool to find the latest or complementary information.
            3. Combine insights from both sources into one comprehensive answer. 
            - The `sources` field must contain ONLY URLs of pages you used (Wikipedia + web results).
            - Put full links starting with https://
            4. Finally, use the save_text_to_file tool to save the structured research data.
            Wrap the output in this format and provide no other text:
            {format_instructions}
            """,
        ),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

# Create the agent using the classic tool-calling API
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


def main():
    query = input("What can I help you search? ")

    # If you don't have chat history yet, just pass an empty list
    raw_response = agent_executor.invoke({"input": query, "chat_history": []})

    try:
        structured_response = parser.parse(raw_response["output"])
        print(structured_response)
    except Exception as e:
        print("Error parsing response:", e)
        print("Raw Response:", raw_response)


if __name__ == "__main__":
    main()


