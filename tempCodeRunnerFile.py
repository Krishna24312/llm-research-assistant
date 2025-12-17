from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic : str
    summary:str
    sources : list[str]
    tools_used : list[str]

llm=ChatOpenAI(model="gpt-4o-mini")
# llm2 = ChatAnthropic(model="claude-3-5-sonnet-20241022")
parser= PydanticOutputParser(pydantic_object=ResearchResponse)
prompt = ChatPromptTemplate.from_messages( #understand this part more carefully
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. Give the answer in 500-1000 words
            For every user query:
            1. First, use the wikipedia tool to get a solid background summary.
            2. Then, use the web-search tool to find the latest or complementary information.
            3. Combine insights from both sources into one comprehensive answer. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())
tools =[search_tool, wiki_tool,save_tool]
agent=create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)
agent_executor= AgentExecutor(agent=agent,tools=tools, verbose=True)
query= input("What can I help you search? ")
raw_response= agent_executor.invoke({"query":query})
try:
    structured_response = parser.parse(raw_response["output"])
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)

