from django.urls import path
from api.views import citizen

urlpatterns = [
    path('citizens/', citizen, name='citizen'),
]
