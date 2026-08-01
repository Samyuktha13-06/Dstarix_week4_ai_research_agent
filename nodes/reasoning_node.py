from graph.state import ResearchState
from utils.llm import llm


def reasoning_node(state: ResearchState):

    prompt = f"""
You are an AI Research Assistant.

A user asked:

{state["question"]}

The following search results were retrieved:

{state["search_results"]}

Read the search results carefully.

Produce a concise, accurate summary that answers the user's question.

Do not include unnecessary information.
"""

    response = llm.invoke(prompt)

    state["summary"] = response.content

    return state