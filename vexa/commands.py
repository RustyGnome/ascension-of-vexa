# The Ascension of Vexa
# Command Processing Module
# Version 0.4

def process_command(command):

    if command == "hello":
        print("Vexa > Greetings, Captain!")

    elif command == "status":
        print("Vexa > All systems operational!")

    elif command == "mission":
        print("Vexa > Our mission is to build an open-source AI assistant.")

    elif command == "help":
        print("Vexa > Available commands: hello, status, mission, help, exit")

    elif command == "exit":
        print("Vexa > Until next time, Captain!")
        return False

    else:
        print("Vexa > Unknown command. Type 'help' for assistance.")

    return True