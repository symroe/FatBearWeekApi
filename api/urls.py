from django.urls import path, include
from rest_framework import routers

from bears.views import BearViewSet

router = routers.DefaultRouter()
router.register(r'bears', BearViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
