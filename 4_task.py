from typing import Dict


def input_error(func):
    def inner(*args, **kwargs):
        try:

            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Enter the argument for the command."
    return inner


@input_error
def add_contact(args: list, contacts: Dict[str, str]) -> str:
    """Add a new contact to the dictionary."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list, contacts: Dict[str, str]) -> str:
    """Change an existing contact's phone number."""
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def phone_contact(args: list, contacts: Dict[str, str]) -> str:
    """Show phone number for a specific contact."""
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"


@input_error
def all_contacts(args: list, contacts: Dict[str, str]) -> str:
    """Show all contacts."""
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def parse_input(user_input: str) -> tuple[str, list]:
    """Parse the user input into command and arguments."""
    cmd, *args = user_input.strip().split()
    cmd = cmd.lower()
    return cmd, args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))
        elif command == "all":
            print(all_contacts(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
