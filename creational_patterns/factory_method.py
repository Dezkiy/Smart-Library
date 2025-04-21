from abc import ABC, abstractmethod

# Abstract Product
class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message: str, recipient: str):
        pass

# Concrete Products
class EmailSender(NotificationSender):
    def send_notification(self, message: str, recipient: str):
        print(f"[Email] To: {recipient} | Message: {message}")

class SMSSender(NotificationSender):
    def send_notification(self, message: str, recipient: str):
        print(f"[SMS] To: {recipient} | Message: {message}")

# Creator
class Notifier(ABC):
    @abstractmethod
    def create_sender(self) -> NotificationSender:
        pass

    def notify(self, message: str, recipient: str):
        sender = self.create_sender()
        sender.send_notification(message, recipient)

# Concrete Creators
class EmailNotifier(Notifier):
    def create_sender(self) -> NotificationSender:
        return EmailSender()

class SMSNotifier(Notifier):
    def create_sender(self) -> NotificationSender:
        return SMSSender()