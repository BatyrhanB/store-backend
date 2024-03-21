from django.template.loader import render_to_string

from common.smtp.email import EmailThread


class EmailService:
    @staticmethod
    def send_email(
        email,
        verifcation_link,
    ) -> None:
        """
        Send email verifcation_link

        :args:
            email (_type_): _message will send to this email_
            verifcation_link (_type_): _link to verify user's account_
        """

        html_template = "email_message.html"
        context = {
            "email": email,
            "verification_link": verifcation_link,
        }
        html_content = render_to_string(html_template, context)
        EmailThread(
            subject=f"User verification {email}",
            html_content=html_content,
            recipient_list=[email],
        ).start()
