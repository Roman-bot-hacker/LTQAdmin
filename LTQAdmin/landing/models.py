from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=80)


class Level(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_name = models.CharField(max_length=80)


class Quest(models.Model):
    quest_id = models.AutoField(primary_key=True)
    quest_name = models.CharField(max_length=80)
    category_id = models.ManyToManyField(Category)
    level_id = models.ForeignKey(Level, on_delete=models.DO_NOTHING)
    quest_image_URL = models.URLField(blank=True)
    distance = models.FloatField()
    quest_description = models.TextField()


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=128)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location_description = models.TextField()
    location_image_URL = models.URLField(blank=True)
    quest_id = models.ManyToManyField(Quest)
    order = models.IntegerField()
    is_secret = models.BooleanField(default=False)





