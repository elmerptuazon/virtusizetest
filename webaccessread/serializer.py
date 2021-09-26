from rest_framework import serializers
from .models import WebAccessRead

class WebAccessReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebAccessRead
        fields = '__all__'
        # fields = ('link', 'word')