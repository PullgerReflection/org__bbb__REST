from rest_framework import serializers
from pullgerReflection.org__bbb import models


class CityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'
