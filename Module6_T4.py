from typing import Dict, List, Tuple


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    parts = user_input.strip().split()

    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."

    return "Contact not found."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    name = args[0]

    if name in contacts:
        return contacts[name]

    return "Contact not found."


def show_all(contacts: Dict[str, str]) -> str:
    if not contacts:
        return "No contacts saved."

    result: List[str] = []

    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)


def main() -> None:
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid command.")
            else:
                print(add_contact(args, contacts))
        elif command == "change":
            if len(args) != 2:
                print("Invalid command.")
            else:
                print(change_contact(args, contacts))
        elif command == "phone":
            if len(args) != 1:
                print("Invalid command.")
            else:
                print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
