from rest_framework_mongoengine import viewsets
from .serializers import NoticeSerializer
from .models import Notice


class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
