from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc.name),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-08-20')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-08-19')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2025-08-18')
        Activity.objects.create(user=users[3], type='Yoga', duration=50, date='2025-08-17')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='Medium')
        Workout.objects.create(name='Plank', description='Hold plank for 1 min', difficulty='Hard')



