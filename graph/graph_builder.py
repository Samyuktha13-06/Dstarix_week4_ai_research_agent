# pyrefly: ignore [missing-import]
from langgraph.graph import StateGraph, START, END

from graph.state import ResearchState


def search_node(state: ResearchState):
    print("Searching...")

    state["search_results"] = (
        f"Dummy search results for: {state['question']}"
    )

    return state


def summary_node(state: ResearchState):
    print("Summarizing...")

    state["summary"] = (
        f"Summary based on: {state['search_results']}"
    )

    return state


builder = StateGraph(ResearchState)

builder.add_node("search", search_node)
builder.add_node("summary", summary_node)

builder.add_edge(START, "search")
builder.add_edge("search", "summary")
builder.add_edge("summary", END)

graph = builder.compile()