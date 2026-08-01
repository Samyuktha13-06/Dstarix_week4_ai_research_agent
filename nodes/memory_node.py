from graph.state import ResearchState


def memory_node(state: ResearchState):

    history = state.get("history", [])

    history.append(
        f"User: {state['question']}"
    )

    if state["summary"]:

        history.append(
            f"Assistant: {state['summary']}"
        )

    state["history"] = history

    return state