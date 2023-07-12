from rest_framework.settings import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_html_email(subject, html_template_path, html_context, recipients):
    email_from = settings.EMAIL_HOST_USER
    html_content = render_to_string(html_template_path, html_context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        # subject
        subject,
        # content
        text_content,
        # from email
        email_from,
        # recipient
        recipients
    )
    # send_mail(subject, "from roman", email_from,
    #           ["razzroman98@gmail.com"])
    email.attach_alternative(html_content, "text/html")
    email.send()
