import json
from pathlib import Path
import os
import tempfile

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MEMORY_FILE = PROJECT_ROOT / "data" / "memory.json"



def load_memory():
    """Load memory, creating a new database if needed."""

    if not MEMORY_FILE.exists():
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        save_memory({})

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)



def save_memory(memory):
    """Safely save memory using atomic replacement."""

    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=MEMORY_FILE.parent,
            delete=False
        ) as temp_file:
            temp_path = Path(temp_file.name)
            json.dump(memory, temp_file, indent=2)
            temp_file.flush()
            os.fsync(temp_file.fileno())

        os.replace(temp_path, MEMORY_FILE)

    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)



def remember(key, value):
    """Store or update a memory."""

    memory = load_memory()
    memory[key] = value
    save_memory(memory)


def recall(key):
    """Retrieve a memory."""

    memory = load_memory()
    return memory.get(key)