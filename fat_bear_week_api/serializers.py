from rest_framework import serializers
from .models import Bear, Bracket, Result

class BearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bear
        fields = ["bear_uuid", "bear_number", "bear_name", "bear_gender", "first_identified", "bear_size",
                  "fur_description", "muzzle_description", "ear_description"]


class BasicBearSerializer(serializers.Serializer):
    bear_uuid = serializers.UUIDField()
    bear_number = serializers.IntegerField()
    bear_name = serializers.CharField()


class ResultSerializer(serializers.Serializer):
    winner = BasicBearSerializer()
    # bracket_id = serializers.IntegerField()
    bracket_date = serializers.StringRelatedField(source="bracket.bracket_date")
    # round = serializers.StringRelatedField(source="bracket.round.final_round")

    class Meta:
        model = Result
        fields = ["winner", "bracket_id", "bracket_date"]

