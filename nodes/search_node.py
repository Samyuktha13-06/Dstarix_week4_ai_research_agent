# pyrefly: ignore [missing-import]
from graph.state import ResearchState
from tools.search_tool import search_tool


def search_node(state: ResearchState):
    query = state["question"]

    print(f"\nSearching for: {query}\n")

    results = search_tool.invoke(query)

    state["search_results"] = str(results)

    return state