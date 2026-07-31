# pyrefly: ignore [missing-import]
from graph.graph_builder import graph

result = graph.invoke(
    {
        "question": "Latest developments in LangGraph",
        "search_results": "",
        "summary": "",
    }
)

print(result["summary"])