from creational_patterns.factory_method import EmailNotifier, SMSNotifier, EmailSender, SMSSender


def test_email_notifier_creation():
    email_notifier = EmailNotifier().create_sender()
    assert isinstance(email_notifier, EmailSender)


def test_sms_notifier_creation():
    sms_notifier = SMSNotifier().create_sender()
    assert isinstance(sms_notifier, SMSSender)


def test_email_notification_send(capsys):
    email_notifier = EmailNotifier().create_sender()
    email_notifier.send_notification("Test Email", "test@example.com")
    captured = capsys.readouterr()
    assert "[Email] To: test@example.com | Message: Test Email" in captured.out


def test_sms_notification_send(capsys):
    sms_notifier = SMSNotifier().create_sender()
    sms_notifier.send_notification("Test SMS", "+1234567890")
    captured = capsys.readouterr()
    assert "[SMS] To: +1234567890 | Message: Test SMS" in captured.out
