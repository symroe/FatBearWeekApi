from django.urls import path, include
from rest_framework import routers

from bears.views import BearViewSet, ChampionsViewSet, FinalistsViewSet

router = routers.DefaultRouter()
router.register(r"bears", BearViewSet)
router.register(r"champions", ChampionsViewSet, basename="champions")
router.register(r"finalists", FinalistsViewSet, basename="finalists")


urlpatterns = [
    path("api/", include(router.urls)),
]
