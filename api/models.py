from django.db import models

class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
