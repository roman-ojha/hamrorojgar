from django.urls import path
from api.views import Citizen

urlpatterns = [
    path('citizens/', Citizen.as_view(), name='citizen'),
]
