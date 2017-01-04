# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import NormalUser, RunResultsTable


class NormalUserInline(admin.StackedInline):
    model = NormalUser
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    inlines = NormalUserInline


@admin.register(RunResultsTable)
class EditRunResults(admin.ModelAdmin):
    pass  # TODO change headers and parameters name visible in admin panel


