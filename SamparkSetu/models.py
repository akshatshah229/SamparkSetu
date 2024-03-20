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

class FormModel(models.Model):
    listing_choices = (('buy','Buy'),('sell','Sell'),('rent','Rent'))
    apartment_choices = (('1bhk','1BHK'),('2bhk','2BHK'),('3bhk','3BHK'),('other','Other'))
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=15)
    listings = models.CharField(max_length=50, choices=listing_choices, default=1)
    apartment = models.CharField(max_length=50, choices=apartment_choices, default=1)
    location = models.CharField(max_length=2000)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.first_name