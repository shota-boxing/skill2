from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams

        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name, is_superhero=True),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel.name, is_superhero=True),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc.name, is_superhero=True),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc.name, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name, is_superhero=True),
        ]

        # Create activities
        from datetime import date
        for user in users:
            Activity.objects.create(user=user.email, type='Running', duration=30, date=date.today())
            Activity.objects.create(user=user.email, type='Cycling', duration=45, date=date.today())

        # Create workouts
        Workout.objects.create(name='Full Body', description='All muscle groups', difficulty='Medium')
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio', difficulty='Hard')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel.name, points=100, rank=1)
        Leaderboard.objects.create(team=dc.name, points=90, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
