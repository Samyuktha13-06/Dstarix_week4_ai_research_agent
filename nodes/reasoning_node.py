from graph.state import ResearchState
from utils.llm import llm


def reasoning_node(state: ResearchState):

    history = "\n".join(
        state.get("history", [])
    )

    prompt = f"""
You are an AI Research Assistant.

Previous Conversation:

{history}

Current Question:

{state["question"]}

Search Results:

{state["search_results"]}

Use the previous conversation whenever it helps answer the user's question.

Provide a concise and accurate response.
"""

    response = llm.invoke(prompt)

    state["summary"] = response.content

    return state