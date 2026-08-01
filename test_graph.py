from graph.graph_builder import graph

state = {
    "question": "What is LangGraph?",
    "search_results": "",
    "summary": "",
    "route": "",
    "history": []
}

result = graph.invoke(state)

state = result

state["question"] = "Who developed it?"

result = graph.invoke(state)
print("\nConversation History:\n")

for item in result["history"]:
    print(item)