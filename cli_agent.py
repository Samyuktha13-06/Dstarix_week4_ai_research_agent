# pyrefly: ignore [missing-import]
from agents.research_agent import ResearchAgent


def main():

    print("=" * 70)
    print("🤖 AI Research Agent")
    print("=" * 70)
    print("Ask any research question.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    agent = ResearchAgent()

    while True:

        question = input("You: ").strip()

        if not question:
            print("Agent: Please enter a question.\n")
            continue

        if question.lower() in ["exit", "quit"]:

            print("\nAgent: Goodbye! 👋")

            break

        try:

            answer = agent.ask(question)

            print(f"\nAgent:\n{answer}\n")

        except Exception as e:

            print(f"\nError: {e}\n")


if __name__ == "__main__":

    main()