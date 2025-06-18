import os
from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from ..tools.tools import get_topic_url

load_dotenv()



def lookup(topic: str) -> str:
    llm = ChatOllama(
        model=os.getenv("LLM"),
        temperature=int(os.getenv("LLM_TEMPERATURE"))
    )

    template = """Given the topic "{topic}", return only the direct URL to the most relevant English Wikipedia page.
Respond with just the full URL, and nothing else. Do not explain. Do not format as markdown. Just return the plain Wikipedia link."""

    prompt_template = PromptTemplate(
        input_variables=["topic"],
        template=template
    )

    tools_for_agent = [
        Tool(
            name="Wikipedia Search Tool",
            func=get_topic_url,
            description="Useful for when you need to get the direct English Wikipedia page URL for a given topic"
        )
    ]

    # Downloading the ReAct prompt - https://www.promptingguide.ai/techniques/react
    react_prompt = hub.pull("hwchase17/react")


    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        handle_parsing_errors=True,
        verbose=True
    )

    result = agent_executor.invoke(
        input={
            "input": prompt_template.format_prompt(topic=topic)
        }
    )

    wikipedia_link = result["output"]

    return wikipedia_link
