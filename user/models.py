from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="details")
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10)
    college = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=25)
    tricity_resident = models.BooleanField(default=True)
    need_stay = models.BooleanField(default=False)
    image_url = models.URLField()

    def __str__(self):
        return self.user.email


class UserRounds(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="rounds")
    registered_round_one = models.BooleanField(default=False)
    selected_round_two = models.BooleanField(default=False)
    registered_round_two = models.BooleanField(default=False)
    selected_round_three = models.BooleanField(default=False)
    registered_round_three = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
