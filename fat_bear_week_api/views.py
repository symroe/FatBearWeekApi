# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bear, Bracket, Result
from .serializers import BearSerializer, ResultSerializer

class BearsView(APIView):
    def get(self, request, *args, **kwargs):
        bears = Bear.objects.all().order_by("bear_number")
        serializer = BearSerializer(bears, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChampionsView(APIView):
    def get(self, request, *args, **kwargs) :
        results = Result.objects.filter(bracket__round__final_round=True).all().order_by("-bracket__bracket_date")
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FinalistsView(APIView):
    def get(self, request, *args, **kwargs):
        bear_1_query = Bracket.objects.filter(round__final_round=True).values('first_bear').all()
        bear_2_query = Bracket.objects.filter(round__final_round=True).values('second_bear').all()
        subquery = bear_1_query.union(bear_2_query)
        bears = Bear.objects.filter(id__in=subquery).all()
        serializer = BearSerializer(bears, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
