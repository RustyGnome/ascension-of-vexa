import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MEMORY_FILE = PROJECT_ROOT / "data" / "memory.json"


def load_memory():
    """Load Vexa's persistent memory."""

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_memory(memory):
    """Save Vexa's memory to disk."""

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=2)


def remember(key, value):
    """Store or update a memory."""

    memory = load_memory()
    memory[key] = value
    save_memory(memory)


def recall(key):
    """Retrieve a memory."""

    memory = load_memory()
    return memory.get(key)