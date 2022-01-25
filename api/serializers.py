from rest_framework import serializers

from subs.models import Subscription, City

class SubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('period','user','city')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id','name','temperature', 'humidity',)


