from rest_framework_mongoengine import serializers
from .models import Notice


class NoticeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
