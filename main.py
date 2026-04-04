from orchestrator.orchestrator import Orchestrator

def main():
    orchestrator = Orchestrator()

    while True:
        user_prompt = input("\nEnter your request (type 'exit' to quit): ")

        if user_prompt.lower() == "exit":
            break

        result = orchestrator.handle_request(user_prompt)

        print("\n=== FINAL OUTPUT ===\n")
        print(result)

        print("\n=== MEMORY ===\n")
        print(orchestrator.memory.get_history())


if __name__ == "__main__":
    main()