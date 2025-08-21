from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)


class Activity(models.Model):
    user = models.CharField(max_length=100)  # Store user name or email
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()


class Leaderboard(models.Model):
    team = models.CharField(max_length=50)  # Store team name
    points = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
