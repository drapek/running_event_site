# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import NormalUser, RunResultsTable


@admin.register(NormalUser)
class NormalUserInline(admin.ModelAdmin):
    can_delete = False
    list_display = ( 'user_id_', 'user_username', 'user_first_name', 'user_last_name', 'user_email', 'sex', 'team_name', 'birth_date', 'telephone', 'event_paid', 'user_is_active', 'event_photo_user_id')
    search_fields = ['question_text']


@admin.register(RunResultsTable)
class EditRunResults(admin.ModelAdmin):
    list_display = ('user_id', 'runner_id', 'user_first_name', 'user_last_name', 'time_5km', 'time_overall')


