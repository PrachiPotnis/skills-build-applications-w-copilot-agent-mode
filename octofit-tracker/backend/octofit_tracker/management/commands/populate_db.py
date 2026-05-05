from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        # Create Users
        ironman = User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel)
        captain = User.objects.create(email='captain@marvel.com', username='Captain America', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, activity_type='run', duration=30, date=date(2026, 5, 1))
        Activity.objects.create(user=captain, activity_type='cycle', duration=45, date=date(2026, 5, 2))
        Activity.objects.create(user=batman, activity_type='swim', duration=25, date=date(2026, 5, 3))
        Activity.objects.create(user=superman, activity_type='fly', duration=60, date=date(2026, 5, 4))

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body strength')
        squats = Workout.objects.create(name='Squats', description='Lower body strength')
        pushups.suggested_for.add(marvel, dc)
        squats.suggested_for.add(marvel, dc)

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
