from graph.state import ResearchState
from utils.llm import llm


def reasoning_node(state: ResearchState):

    history = "\n".join(state.get("history", []))

    if state["search_results"]:

        prompt = f"""
You are an AI Research Assistant.

Previous Conversation:
{history}

User Question:
{state["question"]}

Search Results:
{state["search_results"]}

Answer ONLY using the search results.
Summarize clearly.
"""

    else:

        prompt = f"""
You are an AI Research Assistant.

Previous Conversation:
{history}

User Question:
{state["question"]}

No web search was performed.

Answer using your general knowledge.
"""

    response = llm.invoke(prompt)

    state["summary"] = response.content

    return state