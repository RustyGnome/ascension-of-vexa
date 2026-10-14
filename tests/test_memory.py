
import unittest
from vexa.memory import remember, recall


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
       
