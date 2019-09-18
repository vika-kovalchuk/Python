from django.contrib import admin
from django.urls import path, include

import MyLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include(MyLogin.urls)),
]