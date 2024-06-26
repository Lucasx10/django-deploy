from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
