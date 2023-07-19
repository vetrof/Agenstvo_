from django.core.mail import EmailMessage
from django.shortcuts import render


def test_mail(request):

    return render(request, 'test_mail.html')


