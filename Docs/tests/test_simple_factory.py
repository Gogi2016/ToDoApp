import unittest
from creational_patterns.simple_factory import TaskFactory

class TestSimpleFactory(unittest.TestCase):
    def test_create_task(self):
        task = TaskFactory.create_task("Assignment")
        self.assertEqual(task.task_type, "Assignment")
