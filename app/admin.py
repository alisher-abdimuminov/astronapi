from django.contrib import admin

from .models import Counter


@admin.register(Counter)
class CounterModelAdmin(admin.ModelAdmin):
    list_display = ["date", "count"]

