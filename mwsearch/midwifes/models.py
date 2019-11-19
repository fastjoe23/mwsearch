from django.db import models

# Create your models here.

class MWRequest(models.Model):
    postcode = models.CharField(max_length=5, default="71334")
    birth_date = models.DateField()

class Midwife(models.Model):
    name = models.CharField(max_length=30, default= "Marie Musterhebamme")
    served_postcode_1 = models.CharField(max_length=5, default="71334")
    served_postcode_2 = models.CharField(max_length=5, default="71332")
    served_postcode_3 = models.CharField(max_length=5, default="71336")

    def __str__(self):
        return self.name
