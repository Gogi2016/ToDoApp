import unittest
from creational_patterns.prototype import Task

class TestPrototypePattern(unittest.TestCase):
    def test_clone_task(self):
        original = Task("Original Task")
        clone = original.clone()
        self.assertIsNot(original, clone)
        self.assertEqual(original.title, clone.title)
