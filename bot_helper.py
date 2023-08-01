import re

STOP_LIST = ("good bye", "close", "exit")
contacts = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except (IndexError, AttributeError):
            return "Wrong command."
        except ValueError:
            return "Data entered incorrectly."
    return inner


def user_input_split(user_input):
    matches = re.match(r'\w+\s+(\D+)\s([+]?\d{7,15})', user_input)
    if matches:
        name = matches.group(1)
        phone = matches.group(2)
        return name, phone
    else:
        return "No data."


def handle_hello():
    return "How can I help you?"


@input_error
def handle_add(user_input):
    name, phone = user_input_split(user_input)
    contacts[name] = phone
    return f"Contact {name} was saved with phone number {phone}.\n"


@input_error
def handle_change(user_input):
    name, phone = user_input_split(user_input)
    contacts[name] = phone
    return f"Contact {name} has been changed. New phone number {phone}.\n"


@input_error
def handle_phone(user_input):
    name = re.match(r'\w+\s+(\D+)', user_input).group(1)
    phone = contacts[name]
    return f"Contact {name}: {phone}\n"


def handle_showall():
    if not contacts:
        return "Contacts book is empty"
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result


def main():
    while True:
        user_input = input("Please enter the command: ")
        if user_input in STOP_LIST:
            print("Good bye!")
            break
        elif user_input.lower() == "hello":
            response = handle_hello()
        elif re.search(r"^add ", user_input, re.IGNORECASE):

            response = handle_add(user_input)
        elif re.search(r"^change ", user_input, re.IGNORECASE):
            response = handle_change(user_input)
        elif re.search(r"^phone ", user_input, re.IGNORECASE):
            response = handle_phone(user_input)
        elif user_input.lower() == "show all":
            response = handle_showall()
        else:
            response = "Wrong command."
        print(response)


if __name__ == "__main__":
    main()
