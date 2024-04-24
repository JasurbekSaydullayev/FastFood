from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'first_name', 'last_name')
    search_fields = ('phone_number', 'email', 'first_name', 'last_name')
