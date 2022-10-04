import csv

from django.conf import settings
from django.core.management import BaseCommand

from bears.models import Bear, Bracket, Round, BracketContestant, Result


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.data_path = settings.BASE_DIR.parent / "database"
        self.import_bears()
        self.import_rounds()
        self.import_brackets()
        self.import_bracket_contestant()
        self.import_results()

    def import_bears(self):
        bears_csv = self.data_path / "bears.csv"
        for line in csv.DictReader(bears_csv.open()):
            bear_number = line.pop("bear_number", None)
            if not bear_number:
                bear_number = None
            line["bear_number"] = bear_number
            line["first_identified"] = line["first_identified"] or None
            Bear.objects.update_or_create(pk=line.pop("id"), defaults=line)

    def import_rounds(self):
        rounds_csv = self.data_path / "rounds.csv"
        for line in csv.DictReader(rounds_csv.open()):
            Round.objects.update_or_create(pk=line.pop("id"), defaults=line)

    def import_brackets(self):
        brackets_csv = self.data_path / "brackets.csv"
        for line in csv.DictReader(brackets_csv.open()):
            Bracket.objects.update_or_create(pk=line.pop("id"), defaults=line)

    def import_bracket_contestant(self):
        bracket_contestant = self.data_path / "bracket_contestants.csv"
        for line in csv.DictReader(bracket_contestant.open()):
            BracketContestant.objects.update_or_create(pk=line.pop("id"), defaults=line)

    def import_results(self):
        results = self.data_path / "results.csv"
        for line in csv.DictReader(results.open()):
            line["winner_id"] = line.pop("winner")
            line["runner_up_id"] = line.pop("runner_up")
            line["winner_votes"] = line["winner_votes"] or None
            line["runner_up_votes"] = line["runner_up_votes"] or None
            Result.objects.update_or_create(pk=line.pop("id"), defaults=line)
