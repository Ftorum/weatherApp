# Generated by Django 4.0.1 on 2022-01-23 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.ImageField(upload_to='cities/', verbose_name='Picture')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('period', models.IntegerField(choices=[('a', 1), ('b', 3), ('c', 6), ('d', 12)], default='d')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs_city', to='subs.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]