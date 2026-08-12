"""Command-line entry point for the AI Business Assistant."""

from .assistant import BusinessAssistant


def main() -> None:
    print("AI Business Assistant")
    print("Describe a business challenge, or type 'quit' to exit.\n")

    assistant = BusinessAssistant()

    while True:
        challenge = input("Business challenge: ").strip()
        if challenge.lower() in {"quit", "exit"}:
            print("Goodbye.")
            break

        try:
            request = assistant.prepare_request(challenge)
            print("\nPrepared AI request:")
            print(request)
            print()
        except ValueError as exc:
            print(f"Input error: {exc}\n")


if __name__ == "__main__":
    main()
