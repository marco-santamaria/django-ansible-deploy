from django.db import models


class Talk(models.Model):
    name = models.CharField(max_length=200)
