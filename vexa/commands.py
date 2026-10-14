# The Ascension of Vexa
# Command Processing Module
# Version 0.4

from vexa.constitution import display_constitution
from vexa.memory import remember, recall
def process_command(command):

    if command == "hello":
        print("Vexa > Greetings, Captain!")

    elif command == "status":
        print("Vexa > All systems operational!")

    elif command == "mission":
        print("Vexa > Our mission is to build an open-source AI assistant.")

    elif command == "help":
        print("Vexa > Available commands:")
        print("  hello         -Greet Vexa")
        print("  status        -Check ship systems")
        print("  mission       -Display our mission")
        print("  constitution  -Display Vexa's principles")
        print("  remember      -Store information (remember key = value)")
        print("  recall        -Retrieve information (recall key)")
        print("  help          -Display available commands")
        print("  exit          -Shut down Vexa")

    elif command == "constitution":
        display_constitution()
    elif command.startswith("remember "):
        data = command[len("remember "):]

        if "=" in data:
            key, value = data.split("=",1)

            key = key.strip()
            value = value.strip()
            if key and value:
                remember(key, value)
                print(f"Vexa > Memory stored: {key}")
            else:
                print("Vexa > Please provide a key and value")
        else:
            print("Vexa > Format: remember key = value")
    elif command.startswith("recall "):
        key = command[len("recall "):].strip()

        if key:
            value = recall(key)

            if value is not None:
                print(f"Vexa > {value}")
            else:
                print(f"Vexa > I don't remember '{key}' yet.")
        else:
            print("Vexa > Please provide a memory key.")


    elif command == "exit":
        print("Vexa > Until next time, Captain!")
        return False

    else:
        print("Vexa > Unknown command. Type 'help' for assistance.")

    return True