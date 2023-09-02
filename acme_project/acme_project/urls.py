from django.contrib import admin
from django.urls import include, path

# Импортировать настройки проекта
from django.conf import settings

# Импортировать функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static


urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
