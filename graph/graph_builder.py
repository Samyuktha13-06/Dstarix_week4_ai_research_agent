# pyrefly: ignore [missing-import]
from langgraph.graph import StateGraph, START, END
from nodes.search_node import search_node
from graph.state import ResearchState
from nodes.search_node import search_node


def summary_node(state: ResearchState):
    state["summary"] = state["search_results"]
    return state


builder = StateGraph(ResearchState)

builder.add_node("search", search_node)
builder.add_node("summary", summary_node)

builder.add_edge(START, "search")
builder.add_edge("search", "summary")
builder.add_edge("summary", END)

graph = builder.compile()