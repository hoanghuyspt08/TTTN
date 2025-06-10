from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    address = models.CharField(max_length=255)
    utilities = models.TextField()
    describe = models.TextField()
    logo = models.TextField()

class Room(models.Model):
    type = models.CharField(max_length=255)
    width = models.IntegerField()
    cost = models.IntegerField()
    utilities = models.TextField()
    image = models.TextField()

