from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=350)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Raincheck(models.Model):
    weekday = models.CharField(max_length=2000)
    is_rain = models.BooleanField(default=False)

    def __str__(self):
        return self.weekday
