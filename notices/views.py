
from rest_framework_mongoengine import viewsets
from .serializers import *
from .models import *


class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
