
# The Ascension of Vexa
# Local AI Neural Interface
# Version 0.1

import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "ornith-1.5:9b"
from pathlib import Path
MODEL_NAME = "ornith-1.5:9b"

def ask_vexa(prompt):
    """Send a prompt to the local Ornith model."""

    
    payload = {
        "model": MODEL_NAME,
        "system": load_identity(),
        "prompt": prompt,
        "stream": False,
        "think": False
    }

    

    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(request, timeout=180) as response:
        result = json.load(response)

    return result.get("response", "")

IDENTITY_FILE = Path(__file__).resolve().parent.parent / "config" / "identity.txt"

def load_identity():
    """Load Vexa's personality instructions from disk."""
    return IDENTITY_FILE.read_text(encoding="utf-8")
