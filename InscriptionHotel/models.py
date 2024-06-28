from django.db import models

# Create your models here.
class Bus(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 =  models.CharField(blank=True, null=True)
    badge_number = models.IntegerField(max_length=50)
    bus_routes = models.IntegerField()
    company_name = models.CharField(max_length=50)
    years_experience =  models.DateField(max_length=50)
    bus_type = models.CharField(max_length=50)



class Client(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 =  models.CharField(max_length=50)



class BusR(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class ClientR(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
