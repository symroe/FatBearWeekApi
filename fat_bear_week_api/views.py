# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bear, Result
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
