from django.db import models

class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
