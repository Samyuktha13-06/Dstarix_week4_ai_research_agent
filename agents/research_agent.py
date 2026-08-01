from graph.graph_builder import graph


class ResearchAgent:

    def __init__(self):

        self.state = {
            "question": "",
            "search_results": "",
            "summary": "",
            "route": "",
            "history": []
        }

    def ask(self, question):

        self.state["question"] = question

        self.state = graph.invoke(self.state)

        return self.state["summary"]