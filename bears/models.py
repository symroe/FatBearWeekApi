from django.db import models


class Bear(models.Model):
    bear_uuid = models.UUIDField()
    bear_number = models.IntegerField(unique=False, blank=True, null=True)
    bear_name = models.TextField(blank=False, null=True)
    bear_gender = models.TextField(blank=True, null=True)
    first_identified = models.IntegerField(blank=True, null=True)
    bear_size = models.TextField(blank=True, null=True)
    fur_description = models.TextField(blank=True, null=True)
    muzzle_description = models.TextField(blank=True, null=True)
    ear_description = models.TextField(blank=True, null=True)


class BracketContestantQuerySet(models.QuerySet):
    def champions(self):
        # TODO: make this query actually do what it should
        return self.filter(bracket__round__final_round=True)

    def finalists(self):
        # TODO: make this query actually do what it should
        return self.filter(bracket__round__final_round=True)


class BracketContestant(models.Model):
    bracket_contestant_uuid = models.UUIDField(blank=True, null=True)
    bracket = models.ForeignKey("Bracket", models.DO_NOTHING, blank=True, null=True)
    bear = models.ForeignKey(Bear, models.DO_NOTHING, blank=True, null=True)

    objects = BracketContestantQuerySet.as_manager()

    class Meta:
        unique_together = (("bracket", "bear"),)


class Bracket(models.Model):
    bracket_uuid = models.UUIDField()
    round = models.ForeignKey("Round", models.DO_NOTHING, blank=True, null=True)
    bracket_date = models.DateField()


class Result(models.Model):
    bracket = models.ForeignKey(Bracket, models.DO_NOTHING)
    winner = models.ForeignKey(
        Bear, models.DO_NOTHING, db_column="winner", related_name="winner"
    )
    winner_votes = models.IntegerField(blank=True, null=True)
    runner_up_votes = models.IntegerField(blank=True, null=True)
    runner_up = models.ForeignKey(
        Bear,
        models.DO_NOTHING,
        db_column="runner_up",
        blank=True,
        null=True,
        related_name="runner_up",
    )


class Round(models.Model):
    round_uuid = models.UUIDField(blank=True, null=True)
    competition_year = models.IntegerField()
    round_number = models.IntegerField(blank=True, null=True)
    final_round = models.BooleanField()

    class Meta:
        unique_together = (("competition_year", "round_number"),)
