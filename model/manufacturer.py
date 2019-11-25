from django.db import models


class manufacturer(models.Model):
    Mername = models.CharField(max_length=50)
    Merother =  models.CharField(max_length=50)