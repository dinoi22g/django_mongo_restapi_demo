from django.db import models
from django.utils import timezone
from mongoengine import *


class Notice(Document):
    title = StringField(max_length=20, required=True, verbose_name='標題')
    content = StringField(required=True, verbose_name='內容')
    created_at = DateTimeField(default=timezone.now, verbose_name='創建日期')

    meta = {'collection': 'notices'}  # 設置集合名稱
