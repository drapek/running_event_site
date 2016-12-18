from django.contrib import admin
from django.contrib.auth.models import User
from .models import NormalUser

class NormalUserInline(admin.StackedInline):
    model = NormalUser
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    inlines = (NormalUserInline)

#Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
