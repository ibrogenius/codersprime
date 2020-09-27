from django.db import models


class Pioneer(models.Model):
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=150)
    about = models.CharField(max_length=1500)
    image = models.FileField()


class Member(models.Model):
    name_mem = models.CharField(max_length=300)
    title_mem = models.CharField(max_length=150)
    about_mem = models.CharField(max_length=1500)
    image_mem = models.FileField()


