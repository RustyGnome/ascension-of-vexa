from vexa.personality import introduce

# Portfolio 1: The Ascension of Vexa
# Version 0.2 - Interactive Command Interface

def greet():
    print("\n================================")
    print("       ASCENSION OF VEXA")
    print("================================")
    print("Vexa Ironvolt Gearbeard reporting!")
    print("Systems online, Captain.\n")


def main():
    greet()
    introduce()

    while True:
        command = input("Captain > ").strip().lower()

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
            break

        else:
            print("Vexa > Unknown command. Type 'help' for assistance.")


if __name__ == "__main__":
    main()
