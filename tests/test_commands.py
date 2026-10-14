# The Ascension of Vexa
# Automated Command Tests

import unittest
from vexa.commands import process_command
import io
from contextlib import redirect_stdout

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
        output = io.StringIO()

        with redirect_stdout(output):
         result = process_command("help")

        self.assertTrue(result)
        self.assertIn("constitution", output.getvalue())

    def test_exit(self):
        result = process_command("exit")
        self.assertFalse(result)

    def test_unknown_command(self):
        result = process_command("unknown")
        self.assertTrue(result)

    def test_constitution(self):
        result = process_command("constitution")
        self.assertTrue(result)
    def test_recall(self):
        output = io.StringIO()

        with redirect_stdout(output):
            result = process_command("recall ship")

        self.assertTrue(result)
        self.assertIn("The Rusty Gnome", output.getvalue())

if __name__ == "__main__":
    unittest.main()