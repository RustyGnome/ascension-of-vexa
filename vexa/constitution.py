# The Ascension of Vexa
# Constitution Loader
# Version 0.5

import json
from pathlib import Path


def load_constitution():
    """Load Vexa's Constitution from its JSON file."""

    project_root = Path(__file__).resolve().parent.parent
    constitution_path = project_root / "config" / "constitution.json"

    with open(constitution_path, "r", encoding="utf-8") as file:
        constitution = json.load(file)

    return constitution


def display_constitution():
    """Display Vexa's constitutional principles."""

    constitution = load_constitution()

    print("\n=== THE VEXA CONSTITUTION ===")
    print(f"Version: {constitution['version']}")
    print(f"Status: {constitution['status']}\n")

    for principle in constitution["core_principles"]:
        print(f"{principle['id']}. {principle['principle']}")
        print(f"   {principle['description']}\n")