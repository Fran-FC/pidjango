from django.contrib import admin
from upv_bot.models import  GymBro
from django import forms


@admin.register(GymBro)
class GymBroAdmin(admin.ModelAdmin):
    list_display = ("user", "dni")