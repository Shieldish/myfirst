from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)   # changed
    last_name = models.CharField(max_length=30)    # changed
    email = models.EmailField()
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15, blank=True, null=True)  # added
    address = models.TextField(blank=True, null=True)  # added
    date_of_birth = models.DateField(blank=True, null=True)  # added


    def __str__(self):
        return f"{self.first_name or ''} {self.last_name or ''} {self.age if self.age is not None else ''}"