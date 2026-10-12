# The Ascension of Vexa
# Automated Command Tests

import unittest
from vexa.commands import process_command


class TestVexaCommands(unittest.TestCase):

    def test_hello(self):
        result = process_command("hello")
        self.assertTrue(result)

    def test_status(self):
        result = process_command("status")
        self.assertTrue(result)

    def test_mission(self):
        result = process_command("mission")
        self.assertTrue(result)

    def test_help(self):
        result = process_command("help")
        self.assertTrue(result)

    def test_exit(self):
        result = process_command("exit")
        self.assertFalse(result)

    def test_unknown_command(self):
        result = process_command("unknown")
        self.assertTrue(result)

    def test_constitution(self):
        result = process_command("constitution")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()