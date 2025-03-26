from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from app.views import count, announcement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('counter/<str:date>/', count,),
    path('announcement/', announcement,),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)