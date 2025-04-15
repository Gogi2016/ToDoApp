from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self):
        pass

class EmailNotification(Notification):
    def notify(self):
        return "Email Notification"

class SMSNotification(Notification):
    def notify(self):
        return "SMS Notification"

class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self):
        pass

class EmailFactory(NotificationFactory):
    def create_notification(self):
        return EmailNotification()

class SMSFactory(NotificationFactory):
    def create_notification(self):
        return SMSNotification()
