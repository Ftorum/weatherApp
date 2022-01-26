from django.core.mail import send_mail
from .models import Subscription
 
from celery import shared_task
from celery.utils.log import get_task_logger
 
logger = get_task_logger(__name__)


def send(user_mail, city_name, city_temperature, city_humidity):
    send_mail(
        'WeatherApp',
        'City: {0}\nTemperature: {1}\nHumidity: {2}'.format(city_name, city_temperature, city_humidity),
        'lacky3462@yandex.ru',
        [user_mail],
        fail_silently=False,
    )

@shared_task()
def thirty_second_func():
    logger.info("I run every 30 seconds using Celery Beat")
    return "Done"

@shared_task()
def send_emails_every_hour():
    subs_every_hour = Subscription.objects.filter(period=1)
    if subs_every_hour.exists():
        for i in subs_every_hour:
            send(i.user.email, i.city, i.city.temperature, i.city.humidity)


@shared_task()
def send_emails_every_tree_hours():
    subs_every_hour = Subscription.objects.filter(period=3)
    for i in subs_every_hour:
        send(i.user.email, i.city, i.city.temperature, i.city.humidity)


@shared_task()
def send_emails_every_six_hours():
    subs_every_hour = Subscription.objects.filter(period=6)
    for i in subs_every_hour:
        send(i.user.email, i.city, i.city.temperature, i.city.humidity)


@shared_task()
def send_emails_every_twelve_hours():
    subs_every_hour = Subscription.objects.filter(period=12)
    for i in subs_every_hour:
        send(i.user.email, i.city, i.city.temperature, i.city.humidity)

