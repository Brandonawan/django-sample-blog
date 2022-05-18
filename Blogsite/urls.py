from django.urls import include, path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
    path('admin/', admin.site.urls), 
    path('', include('articles.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)