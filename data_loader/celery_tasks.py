import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_loader.settings")

task_app = Celery("data_loader")

task_app.config_from_object('django.conf:settings', namespace='CELERY')

task_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
