
import unittest
from vexa.memory import remember, recall, load_memory
import tempfile
from pathlib import Path
from unittest.mock import patch
import json

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
  
    def test_create_missing_memory_file(self):
        self.memory_path.unlink()

        result = load_memory()

        self.assertEqual(result, {})
        self.assertTrue(self.memory_path.exists())

    def test_corrupted_memory_file(self):
        self.memory_path.write_text(
            "{invalid json",
            encoding="utf-8"
        )

        with self.assertRaises(json.JSONDecodeError):
            load_memory()


    def test_failed_save_preserves_memory(self):
        remember("ship", "The Rusty Gnome")

        with patch(
            "vexa.memory.os.replace",
            side_effect=OSError("Simulated disk failure")
        ):
            with self.assertRaises(OSError):
                remember("ship", "Enemy Vessel")

        result = recall("ship")

        self.assertEqual(result, "The Rusty Gnome")
