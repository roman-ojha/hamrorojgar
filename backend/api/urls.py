from django.urls import path
from .views import index

urlpatterns = [
    path('citizens/', index.index, name='index'),
]
