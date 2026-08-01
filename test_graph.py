from graph.graph_builder import graph

result = graph.invoke(
    {
        "question": "Latest developments in LangGraph",
        "search_results": "",
        "summary": "",
        "route": ""
    }
)

print("\nFinal Summary:\n")

print(result["summary"])