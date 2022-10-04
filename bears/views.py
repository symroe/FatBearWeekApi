from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bears.models import Bear, Result, BracketContestant
from bears.serializers import BearSerializer, ContestantSerializer


class BearsView(APIView):
    def get(self, request, *args, **kwargs):
        bear_id = kwargs.get("bear_uuid")
        if bear_id:
            bear = Bear.objects.filter(bear_uuid=bear_id).first()
            serializer = BearSerializer(bear)
        else:
            bears = Bear.objects.all().order_by("bear_number")
            serializer = BearSerializer(bears, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ChampionsView(APIView):
    def get(self, request, *args, **kwargs):
        winner_bear_ids = (
            Result.objects.filter(bracket__round__final_round=True)
            .values("winner")
            .all()
        )
        contestants = BracketContestant.objects.filter(
            bear_id__in=winner_bear_ids
        ).all().distinct("bear_id")
        serializer = ContestantSerializer(contestants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FinalistsView(APIView):
    def get(self, request, *args, **kwargs):
        contestants = (
            BracketContestant.objects.filter(bracket__round__final_round=True)
            .all()
            .distinct("bear_id")
        )
        serializer = ContestantSerializer(contestants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
