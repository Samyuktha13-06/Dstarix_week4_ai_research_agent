from graph.state import ResearchState


def router_node(state: ResearchState):

    question = state["question"].lower()

    search_keywords = [
        "latest",
        "news",
        "research",
        "compare",
        "find",
        "search"
    ]

    if any(word in question for word in search_keywords):

        state["route"] = "search"

    else:

        state["route"] = "summary"

    return state