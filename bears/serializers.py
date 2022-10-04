from rest_framework import serializers
from bears.models import Bear, BracketContestant


class BearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bear
        fields = "__all__"


class BasicBearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bear
        fields = ["bear_uuid", "bear_name", "bear_number"]


class ContestantSerializer(serializers.HyperlinkedModelSerializer):
    bear = BasicBearSerializer()
    bracket_date = serializers.StringRelatedField(source="bracket.bracket_date")

    class Meta:
        model = BracketContestant
        fields = ["bear", "bracket_date"]
