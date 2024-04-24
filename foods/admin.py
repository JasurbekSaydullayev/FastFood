from django.contrib import admin

from foods.models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at', 'image')
