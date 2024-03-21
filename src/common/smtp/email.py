import threading

from django.conf import settings
from django.core.mail import EmailMessage


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run(self) -> None:
        """
        Send email to user in different thread
        """
        msg = EmailMessage(
            subject=self.subject,
            body=self.html_content,
            from_email=settings.EMAIL_HOST_USER,
            to=self.recipient_list,
        )
        msg.content_subtype = "html"
        msg.send()
