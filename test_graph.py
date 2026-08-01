from graph.graph_builder import graph

result = graph.invoke(
    {
        "question": "What is Python?",
        "search_results": "",
        "summary": "",
        "route": ""
    }
)

print(result)