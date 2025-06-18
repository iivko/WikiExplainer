from langchain_tavily import TavilySearch



def get_topic_url(topic: str):
    """Search for and return the most relevant Wikipedia page URL"""

    search = TavilySearch()
    response = search.run(f"site:en.wikipedia.org {topic}")

    return response