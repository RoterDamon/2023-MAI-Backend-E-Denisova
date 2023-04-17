# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Art(models.Model):
    art_id = models.AutoField(primary_key=True)
    name_pic = models.TextField(unique=True)
    artist = models.ForeignKey('Artist', models.DO_NOTHING)
    genre = models.ForeignKey('Genre', models.DO_NOTHING)
    creation_date = models.DateField()
    price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'art'


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    name_artist = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'artist'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name_city = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'city'


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name_client = models.TextField()
    email = models.TextField(unique=True)
    client_password = models.TextField()
    city = models.ForeignKey(City, models.DO_NOTHING)
    role = models.ForeignKey('ClientRole', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'client'


class ClientRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    name_role = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'client_role'


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name_genre = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'genre'
