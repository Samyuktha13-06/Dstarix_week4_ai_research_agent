# pyrefly: ignore [missing-import]
from langgraph.graph import (
    StateGraph,
    START,
    END
)

from graph.state import ResearchState
from nodes.router_node import router_node
from nodes.search_node import search_node
from nodes.reasoning_node import reasoning_node
from nodes.memory_node import memory_node


builder = StateGraph(ResearchState)

builder.add_node("router", router_node)
builder.add_node("search", search_node)
builder.add_node("reason", reasoning_node)
builder.add_node("memory", memory_node)

builder.add_edge(
    START,
    "router"
)

builder.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "search": "search",
        "summary": "reason"
    }
)

builder.add_edge(
    "search",
    "reason"
)

builder.add_edge(
    "reason",
    END
)

builder.add_edge(
    "reason",
    "memory"
)

builder.add_edge(
    "memory",
    END
)


graph = builder.compile()