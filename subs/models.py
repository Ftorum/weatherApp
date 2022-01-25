from http.client import METHOD_NOT_ALLOWED
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='cities/', verbose_name='Picture', null=False)
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return str(self.name)


class Subscription(models.Model):
    CHOICES =(
        (1, 1),
        (3, 3),
        (6, 6),
        (12, 12),
    )
    period = models.PositiveIntegerField(choices=CHOICES, default=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subs_user")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='subs_city')

    def __str__(self):
        return (str(self.user) +': '+ str(self.city))
