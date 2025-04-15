import unittest
from creational_patterns.singleton import AuthSystem

class TestSingletonPattern(unittest.TestCase):
    def test_singleton_instance(self):
        instance1 = AuthSystem()
        instance2 = AuthSystem()
        self.assertIs(instance1, instance2)
