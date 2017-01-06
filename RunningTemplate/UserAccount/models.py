# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


# This class is extension to bulid-in User profile used to authentication.
# It give additional info to users - what is needed to page functionality.
class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # here are additional user parameters
    telephone = models.CharField(max_length=12)  # the longest phone number looks like this +48823123092
    team_name = models.CharField(max_length=254, null=True)
    birth_date = models.DateField()
    sex = models.CharField(max_length=5) # It should store on of values: 'man' or 'woman'.
    event_paid = models.BooleanField(default=False)
    event_photo_user_id = models.CharField(max_length=50)  # user id to external photo service

    class Meta(object):
        verbose_name = "Dodatkowe dane użytkownika"
        verbose_name_plural = "Dodatkowe dane użytkownika"

    def user_id_(self):
        return int(self.user.id)

    def user_username(self):
        return self.user.username

    def user_first_name(self):
        return self.user.first_name

    def user_last_name(self):
        return self.user.last_name

    def user_email(self):
        return self.user.email

    def user_is_active(self):
        return self.user.is_active


class RunResultsTable(models.Model):
    runner_id = models.ForeignKey(User)
    time_5km = models.FloatField('5km_time')
    time_overall = models.FloatField('10km_time')

    class Meta(object):
        verbose_name = "Wynik biegacza"
        verbose_name_plural = "Wyniki biegu"

    def user_first_name(self):
        return self.runner_id.first_name

    def user_last_name(self):
        return self.runner_id.last_name

    def user_id(self):
        return self.runner_id.id
