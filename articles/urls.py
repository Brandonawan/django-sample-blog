from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [

# ]

urlpatterns = [
    # ... the rest of your URLconf goes here ...
    path('articles',views.article_list),
    path('',views.homepage),
    path('about',views.about),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






