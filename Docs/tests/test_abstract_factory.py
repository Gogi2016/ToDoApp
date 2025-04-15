import unittest
from creational_patterns.abstract_factory import WindowsFactory, MacOSFactory, WindowsButton, MacOSButton

class TestAbstractFactory(unittest.TestCase):
    def test_windows_button(self):
        factory = WindowsFactory()
        button = factory.create_button()
        self.assertIsInstance(button, WindowsButton)
        self.assertEqual(button.render(), "Windows Button")

    def test_macos_button(self):
        factory = MacOSFactory()
        button = factory.create_button()
        self.assertIsInstance(button, MacOSButton)
        self.assertEqual(button.render(), "MacOS Button")
