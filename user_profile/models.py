from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)
    location = CountryField()
    birth_date = models.DateField()
    is_protected_acc = models.BooleanField(default=False)
    # followers = models.ManyToManyField(User, db_index=True)

    def __str__(self):
        return f"display_name: {self.display_name} - id: {self.user.username}"
