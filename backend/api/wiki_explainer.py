import os
from typing import Tuple

from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from .agents.wikipedia_lookup_agent import lookup
from .third_parties.wikipedia import wiki_fetcher

from .output_parser import SummaryText, text_parser


load_dotenv()


def explainer(topic: str) -> Tuple[SummaryText, str] | str:
    topic_url = lookup(topic=topic)
    topic_data = wiki_fetcher(topic=topic_url.split("/")[-1])

    explaining_template = """
You are an expert educator. Using the information below, please:

1. Provide a clear, concise explanation of the topic: **{title}**.
2. Then list **three** interesting or surprising facts related to **{title}**.

---  
Information:  
{text}  

Your response should have two sections:

**Explanation:**  
[Write a well‐structured paragraph that covers the essence of the topic.]

**Three Interesting Facts:**  
1. [First fact]  
2. [Second fact]  
3. [Third fact]

{format_instructions}
"""

    explaining_prompt_template = PromptTemplate(
        input_variables=["title", "text"],
        template=explaining_template,
        partial_variables={
            "format_instructions": text_parser.get_format_instructions()
        },
    )

    llm = ChatOllama(
        model=os.getenv("LLM"),
        temperature=os.getenv("LLM_TEMPERATURE")
    )

    chain = explaining_prompt_template | llm | text_parser

    if topic_data["success"]:
        response: SummaryText = chain.invoke(
            input={
                "title": topic_data["topic"],
                "text": topic_data["text"]
            }
        )

        print(topic_url)
        print(topic_data["image_url"])
        return response, topic_data["image_url"]

    return "Nothing found"
