from django.contrib.auth.models import User
from django.db import models


# This class is extension to bulid-in User profile used to authentication.
# It give additional info to users what is needed to page functionality.
class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # here are additional user parameters
    telephone = models.CharField(max_length=12)  # the longest phone number looks like this +48823123092
    team_name = models.CharField(max_length=254, null=True)
    birth_date = models.DateField()
    sex = (
        ('M', 'Men'),
        ('W', 'Women')
    )
    event_paid = models.BooleanField(default=False)
    event_photo_user_id = models.CharField(max_length=50)  # user id to external photo service

