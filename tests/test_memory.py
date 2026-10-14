
import unittest
from vexa.memory import remember, recall
import tempfile
from pathlib import Path
from unittest.mock import patch


class TestVexaMemory(unittest.TestCase):

    def test_remember_and_recall(self):
        remember("test_ship", "The Rusty Gnome")

        result = recall("test_ship")

        self.assertEqual(result, "The Rusty Gnome")

 
    def test_update_memory(self):
        remember("test_location", "Earth")

        remember("test_location", "Mars")

        result = recall("test_location")

        self.assertEqual(result, "Mars")
    
    def test_unknown_memory(self):
        result = recall("unknown_memory_test_12345")

        self.assertIsNone(result)
    
     
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.memory_path = Path(self.temp_dir.name) / "memory.json"
        self.memory_path.write_text("{}", encoding="utf-8")

        self.patcher = patch(
            "vexa.memory.MEMORY_FILE",
            self.memory_path
        )
        self.patcher.start()
        self.addCleanup(self.patcher.stop)
        self.addCleanup(self.temp_dir.cleanup)
  
