from urllib.request import Request

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from zayavki.models import Zayavka


@receiver(post_save, sender=Zayavka)
def send_email_to_manager(sender, instance, created, **kwargs):
    if created:
        subject = 'New zayavka'
        message = f"новая заявка от {instance.name} / тема письма: {instance.question} / email: {instance.email}"
        from_email = 'vetrof@yandex.ru'
        recipient_list = ['vetrof@gmail.com']
        send_mail(subject, message, from_email, recipient_list)