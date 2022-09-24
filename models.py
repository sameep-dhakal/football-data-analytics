# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Country'
# Unable to inspect table 'League'
# The error was: list index out of range
# Unable to inspect table 'Match'
# The error was: list index out of range


class Player(models.Model):
    player_api_id = models.IntegerField(blank=True, null=True)
    player_name = models.TextField(blank=True, null=True)
    player_fifa_api_id = models.IntegerField(blank=True, null=True)
    birthday = models.TextField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Player'
# Unable to inspect table 'Player_Attributes'
# The error was: list index out of range


class Team(models.Model):
    team_api_id = models.IntegerField(blank=True, null=True)
    team_fifa_api_id = models.IntegerField(blank=True, null=True)
    team_long_name = models.TextField(blank=True, null=True)
    team_short_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Team'
# Unable to inspect table 'Team_Attributes'
# The error was: list index out of range
