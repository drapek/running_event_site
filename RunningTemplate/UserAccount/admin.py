# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe
from .models import NormalUser, RunResultsTable
from django.contrib.auth.models import User


class NormalUserInline(admin.StackedInline):
    model = NormalUser
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    inlines = NormalUserInline


@admin.register(RunResultsTable)
class EditRunResults(admin.ModelAdmin):
    list_display = ('user_id', 'runner_id', 'user_first_name', 'user_last_name', 'time_5km', 'time_overall')


