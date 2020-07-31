from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from music.views import GetView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('music/', include('music.urls')),
                  url(r'^getview$', GetView.as_view(), name='get-view')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
