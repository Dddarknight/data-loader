from celery import shared_task
from celery.schedules import crontab
from datetime import timedelta
from django.utils import timezone

from data_loader.celery_tasks import task_app
from data_loader.resources.models import ExpiringLink


@shared_task()
def task_delete_expiring_links():
    for link in ExpiringLink.objects.all():
        if timezone.now() > (
                link.created_at + timedelta(seconds=link.expiring_time)):
            link.delete()


task_app.conf.beat_schedule = {
    'delete_expiring_links': {
        'task': 'data_loader.resources.tasks.task_delete_expiring_links',
        'schedule': crontab(minute="*/60")
    }
}
