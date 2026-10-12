# Portfolio 1: The Ascension of Vexa
# Version 0.5 - Modular Architecture

from vexa.personality import introduce
from vexa.commands import process_command


def greet():
    print("\n================================")
    print("       ASCENSION OF VEXA")
    print("================================")
    print("Vexa Core Systems Online!\n")


def main():
    greet()
    introduce()

    running = True

    while running:
        command = input("Captain > ").strip().lower()
        running = process_command(command)


if __name__ == "__main__":
    main()