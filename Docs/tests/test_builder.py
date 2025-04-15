import unittest
from creational_patterns.builder import UserBuilder

class TestBuilderPattern(unittest.TestCase):
    def test_build_user(self):
        builder = UserBuilder()
        user = builder.set_name("Alice").set_email("alice@example.com").set_password("secure123").build()
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.email, "alice@example.com")
        self.assertEqual(user.password, "secure123")
