from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

# from celery import shared_task

from zayavki.models import Zayavka
from main.models import Realty, Manager


# @shared_task
# def send_email_to_manager(instance_id):
#     instance = Zayavka.objects.get(id=instance_id)
#     manager_email = Manager.objects.get(id=instance.manager_id).email
#     subject = 'New'
#     message = f"новая заявка от {instance.name} / тема письма: {instance.question} / email отправителя: {instance.email}"
#     from_email = 'vetrof@yandex.ru'
#     recipient_list = [manager_email]
#     send_mail(subject, message, from_email, recipient_list)
#
#
# @receiver(post_save, sender=Zayavka)
# def send_email_to_manager_signal(sender, instance, created, **kwargs):
#     if created:
#         send_email_to_manager.delay(instance.id)


@receiver(post_save, sender=Zayavka)
def send_email_to_manager(sender, instance, created, **kwargs):
    if created:
        manager_email = Manager.objects.get(id=instance.manager_id).email
        subject = 'New zayavka'
        message = f"новая заявка от {instance.name} / тема письма: {instance.question} / email отправителя: {instance.email}"
        from_email = 'vetrof@yandex.ru'
        recipient_list = [manager_email]
        send_mail(subject, message, from_email, recipient_list)
