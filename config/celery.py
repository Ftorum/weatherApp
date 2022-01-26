import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
# app.conf.timezone = 'Europe/London'
 
app.conf.beat_schedule = {
    "every_hour": {
        "task": "subs.tasks.send_emails_every_hour",
        "schedule": timedelta(hours=1),
    },
    "every_tree_hours": {
        "task": "subs.tasks.send_emails_every_tree_hours",
        "schedule": timedelta(hours=3),
    },
    "every_six_hours": {
        "task": "subs.tasks.send_emails_every_six_hours",
        "schedule": timedelta(hours=6),
    },
    "every_twelve_hours": {
        "task": "subs.tasks.send_emails_every_twelve_hours",
        "schedule": timedelta(hours=12),
    },
}
 
app.autodiscover_tasks()