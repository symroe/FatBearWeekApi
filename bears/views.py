from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from bears.models import Bear, Result, BracketContestant
from bears.serializers import BearSerializer, ContestantSerializer


class BearViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bear.objects.all()
    serializer_class = BearSerializer


class ChampionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = BracketContestant.objects.champions()
    serializer_class = ContestantSerializer


class FinalistsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = BracketContestant.objects.finalists()
    serializer_class = ContestantSerializer
