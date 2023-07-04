from django.apps import AppConfig


class ZayavkiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zayavki'

    def ready(self):
        import zayavki.singnals
