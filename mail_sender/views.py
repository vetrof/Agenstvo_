from django.core.mail import EmailMessage
from django.shortcuts import render


def test_mail(request):

    subject = 'test mail'
    message = 'Новая заявка !!!'
    from_email = 'Django@uytuy.ru'
    recipient_list = ['anderzhanova.regina@yandex.ru']
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.send()

    return render(request, 'main.html')


