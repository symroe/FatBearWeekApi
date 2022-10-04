from django.contrib import admin
from django.urls import path, include
from .views import BearsView, ChampionsView, FinalistsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/bears", BearsView.as_view()),
    path("api/bears/<bear_uuid>", BearsView.as_view()),
    path("api/champions", ChampionsView.as_view()),
    path("api/finalists", FinalistsView.as_view()),
]
