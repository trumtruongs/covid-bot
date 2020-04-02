from rest_framework import serializers
from welcome import models


class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Welcome
        fields = '__all__'

