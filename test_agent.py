from agents.research_agent import ResearchAgent

agent = ResearchAgent()

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:

        break

    answer = agent.ask(question)

    print("\nAgent:")

    print(answer)