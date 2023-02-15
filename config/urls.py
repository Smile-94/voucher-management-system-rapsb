
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# app urls
from accounts import urls as accouts_urls
from authority import urls as authority_usrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(accouts_urls)),
    path('', include(authority_usrls)),
]

# for serve static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
