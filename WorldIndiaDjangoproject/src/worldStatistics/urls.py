from django.urls import include,path
from .views import (
    trends,
    top5
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('top5/', top5,name='top5'),
    path('trends/', trends,name='trends'),
]
urlpatterns+=staticfiles_urlpatterns()