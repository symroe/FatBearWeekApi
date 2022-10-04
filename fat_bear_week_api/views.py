# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bear, Bracket, Result, BracketContestant
from .serializers import BearSerializer, ResultSerializer


class BearsView(APIView):
    def get(self, request, *args, **kwargs):
        bear_id = kwargs.get('bear_uuid')
        if bear_id:
            bear = Bear.objects.filter(bear_uuid=bear_id).first()
            serializer = BearSerializer(bear)
        else:
            bears = Bear.objects.all().order_by("bear_number")
            serializer = BearSerializer(bears, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ChampionsView(APIView):
    def get(self, request, *args, **kwargs) :
        winner_ids = Result.objects.filter(bracket__round__final_round=True).values('winner').all()
        bears = Bear.objects.filter(id__in=winner_ids).all()
        serializer = BearSerializer(bears, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FinalistsView(APIView):
    def get(self, request, *args, **kwargs):
        bear_ids = BracketContestant.objects.filter(bracket__round__final_round=True).values('bear_id').all()
        bears = Bear.objects.filter(id__in=bear_ids).all()
        serializer = BearSerializer(bears, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
