# tests/test_dialogue_generator.py

import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from synthetic_dialogue.dialogue_generator import DialogueGenerator

class TestDialogueGenerator(unittest.TestCase):
    def test_generate_dialogue(self):
        generator = DialogueGenerator()
        roles = ["Analyst", "Attacker", "Defender"]
        dialogue = generator.generate(roles)
        self.assertEqual(len(dialogue), 3)
        self.assertEqual(dialogue[0]["role"], "Analyst")
        self.assertIn("Investigate", dialogue[0]["intent"])

if __name__ == "__main__":
    unittest.main()
