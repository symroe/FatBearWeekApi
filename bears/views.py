from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from bears.models import Bear, Result, BracketContestant
from bears.serializers import BearSerializer, ContestantSerializer


class BearViewSet(viewsets.ModelViewSet):
    queryset = Bear.objects.all()
    serializer_class = BearSerializer


class ChampionsView(APIView):
    def get(self, request, *args, **kwargs):
        champions = BracketContestant.objects.champions()
        serializer = ContestantSerializer(champions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FinalistsView(APIView):
    def get(self, request, *args, **kwargs):
        finalists = BracketContestant.objects.finalists()
        serializer = ContestantSerializer(finalists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
