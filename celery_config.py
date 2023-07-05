# celery_config.py

import os
from celery import Celery

# Установите переменную окружения DJANGO_SETTINGS_MODULE, если она не установлена
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

# Создайте экземпляр приложения Celery
app = Celery('your_project_name')

# Загрузите настройки конфигурации Django для Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Обнаружение и регистрация задач в приложениях Django
app.autodiscover_tasks()

# Определите функцию, чтобы Celery мог найти задачи в файлах models.py и сигналы
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
