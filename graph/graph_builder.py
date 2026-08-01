# pyrefly: ignore [missing-import]
from langgraph.graph import StateGraph, START, END

from graph.state import ResearchState
from nodes.router_node import router_node
from nodes.search_node import search_node


def summary_node(state: ResearchState):

    if state["search_results"]:

        state["summary"] = state["search_results"]

    else:

        state["summary"] = (
            "No web search was needed."
        )

    return state


builder = StateGraph(ResearchState)

builder.add_node("router", router_node)
builder.add_node("search", search_node)
builder.add_node("summary", summary_node)

builder.add_edge(START, "router")


builder.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "search": "search",
        "summary": "summary"
    }
)

builder.add_edge("search", "summary")
builder.add_edge("summary", END)

graph = builder.compile()