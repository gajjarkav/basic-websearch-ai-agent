# here i am using settings.py{config.py} with pydantic settings for manage all environments
from setting import settings

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# here i am duckduckgo for websearch <which is also free and no api key needed>
from langchain_community.tools import DuckDuckGoSearchRun
# here imported 2 module where you can use openrouter or groq as llm provider <both are optional also work on single api key>
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
# so here i use this built in class in this langchain module for save that session memory <no longterm memory>
from langchain.memory import ConversationBufferWindowMemory

if settings.GROQ_API_KEY:
    print("✅ Using Groq LLM as Provider")
    llm = ChatGroq(model=settings.GROQ_LLM_MODEL, temperature=settings.TEMPERATURE)

elif settings.OPENROUTER_API_KEY:
    print("✅ Using OpenRouter as LLM Provider")
    llm = ChatOpenAI(
        model=settings.OPENROUTER_LLM_MODEL,
        api_key=settings.OPENROUTER_API_KEY,
        temperature=settings.TEMPERATURE,
        base_url="https://openrouter.ai/api/v1"
    )

else:
    print("🚨 No API key found for Groq or OpenRouter!!!!")
    exit()


search_tool = DuckDuckGoSearchRun()

tools = [search_tool]

prompt = ChatPromptTemplate([
    ('system', 'You are a helpful assistant. You have access to a search tool.'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{input}'),
    MessagesPlaceholder(variable_name="agent_scratchpad")]
)

memory = ConversationBufferWindowMemory(
#     it stores last 6 chat convos
    k=6,
    return_messages=True,
    memory_key="chat_history"
)

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    memory=memory,
    agent=agent,
    verbose=True,
    tools=tools
)

print("\n🤖 Agent is ready! Type 'exit' to end the chat.")
while True:
    user_input = input("\nYou : ")
    if user_input.lower() == 'exit':
        print("👋 Goodbye!")
        break
    if user_input:
        response = agent_executor.invoke({"input":user_input})
        print(f"Agent :  {response['output']}")