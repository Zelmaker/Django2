from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register(r'location', LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("user/", include('users.urls')),
    path("", include('ads.urls')),
]

urlpatterns += router.urls
