from django.urls import path, include
from .views import index

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', include('myadmin.urls')),
    # path('admin/', include('admin_argon.urls')),
]
