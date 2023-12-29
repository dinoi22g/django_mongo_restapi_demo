# Django + MongoDB 實作 Restful API

## 設定MongoDB (Linux)

### 1. 設置登入模式=>驗證

**開啟mongod.conf** 
```
sudo vim /etc/mongod.conf
```

**增加授權機制**
```
security:
    authorization: enabled
```

**重啟MongoDB**
```
sudo systemctl restart mongod
```

### 2. 建立資料庫帳號

**執行Mongo shell**
```
mongo
```

**切換資料庫到demo**
```
use demo
```

**建立帳號並開啟對資料庫demo的權限**
```
db.createUser(
  {
    user: "dino",
    pwd: "{PASSWORD}",
    roles: [ { role: "readWrite", db: "demo" } ]
  }
)
```

### Python安裝套件

**忽略Django建立過程**

```
pip install mongoengine==0.27.0
pip install pymongo==3.12.3
pip install djangorestframework==3.14.0
pip install django-rest-framework-mongoengine==3.4.1
```

### 修改settings.py

**註冊APPs**
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_mongoengine',
    'notices' # 此為該範例的App, 可自行使用django-admin startapp建立新的
    ...
]
```

**新增Restful Framework設定**
```
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}
```

**修改Database**

註解掉原本的DATABASE設定或直接留空 (該範例直接註解)
```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#
```

使用mongoengine建立與mongoDB得連線
```
import mongoengine

mongoengine.connect(host="mongodb://dino:X7XaWhnFiy@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=demo", alias='default')
```

### 建立Restful API 

**以本範例的'notice' app示範**

#### 1. 建立Model (notice/models.py)

**將原本採用的models.Model改成mongoengine的Document，Field部分mongoengine也都有支援**
```
from django.utils import timezone
from mongoengine import *


class Notice(Document):
    title = StringField(max_length=20, required=True, verbose_name='標題')
    content = StringField(required=True, verbose_name='內容')
    created_at = DateTimeField(default=timezone.now, verbose_name='創建日期')

    meta = {'collection': 'notices'}  # 設置集合名稱
```

#### 2. 建立Serializer (notice/serializers.py)

**這邊的話就直接採用rest_framework_mongoengine所提供的serializers類**

```
from rest_framework_mongoengine import serializers
from .models import Notice


class NoticeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
```

#### 3. 建立ViewSet (notice/viewsets.py)

```
from rest_framework_mongoengine import viewsets
from .serializers import NoticeSerializer
from .models import Notice

class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
```

#### 4. 建立路由 (urls.py)


```
from rest_framework_mongoengine import routers
from notices.viewsets import NoticeViewSet

router = routers.DefaultRouter()
router.register(r'notice', NoticeViewSet, basename='notice')

urlpatterns = [
    ...
    path('api/', include(router.urls)),
]
```

### 啟動

```
python manage.py runserver 8000
```

### 使用postman等工具驗證

<img width="677" alt="image" src="https://github.com/dinoi22g/django_mongo_restapi_demo/assets/95574882/94976c39-b493-475b-90bf-77a7c833cec6">

### 完成

