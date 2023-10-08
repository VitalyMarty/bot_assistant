class Assistant:

    def __init__(self):
        self.contacts = {}



    @staticmethod
    def input_error(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except KeyError as e:
                return f"Error: Contact not found - {e}"
            except ValueError as e:
                return f"Error: Invalid input - {e}"
            except IndexError as e:
                return f"Error: Invalid input - not enough values to unpack"
            except Exception as e:
                return f"Error: {str(e)}"
        return wrapper

    def run(self):
        print("Bot assistant is running. Type 'exit' to exit.")
        while True:
            command = input("Enter a command: ")
            try:
                result = self.parse_command(command)
                if result:
                    print(result)
            except Exception as e:
                print(f"Error: {str(e)}")

    @input_error
    def parse_command(self, command):
        command = command.lower()
        if command == 'hello':
            return "How can I help you?"
        elif command.startswith('add '):
            _, data = command.split(' ', 1)
            if ' ' not in data:
                return "Give me name and phone please"
            name, phone = data.split()
            self.contacts[name] = phone
            return f"Added contact: {name}, {phone}"
        elif command.startswith('change '):
            _, data = command.split(' ', 1)
            if ' ' not in data:
                return "Give me name and phone please"
            name, phone = data.split()
            if name in self.contacts:
                self.contacts[name] = phone
                return f"Updated contact: {name}, {phone}"
            else:
                raise ValueError(f"Contact '{name}' not found.")
        elif command.startswith('phone '):
            _, name = command.split(' ', 1)
            if name in self.contacts:
                return f"Phone number for {name}: {self.contacts[name]}"
            else:
                raise ValueError(f"Contact '{name}' not found.")
        elif command == 'show all':
            if not self.contacts:
                return "No users found"
            return "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
        elif command in ['good bye', 'close', 'exit']:
            print("Good bye!")
            exit()
        elif command in ['add', 'change']:
            return "Give me name and phone please"
        elif command == 'phone':
            return "Give me name please"
        else:
            raise ValueError("Unknown command.")


if __name__ == "__main__":
    bot = Assistant()
    bot.run()
