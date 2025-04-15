import unittest
from creational_patterns.factory_method import EmailFactory, SMSFactory, EmailNotification, SMSNotification

class TestFactoryMethod(unittest.TestCase):
    def test_email_notification(self):
        factory = EmailFactory()
        notification = factory.create_notification()
        self.assertIsInstance(notification, EmailNotification)
        self.assertEqual(notification.notify(), "Email Notification")

    def test_sms_notification(self):
        factory = SMSFactory()
        notification = factory.create_notification()
        self.assertIsInstance(notification, SMSNotification)
        self.assertEqual(notification.notify(), "SMS Notification")
