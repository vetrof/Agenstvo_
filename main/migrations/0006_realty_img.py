# Generated by Django 4.2.1 on 2023-06-12 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_manager_email_alter_manager_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='realty',
            name='img',
            field=models.ImageField(blank=True, upload_to='house_image'),
        ),
    ]
