from django.contrib import admin

from .models import Counter, Announcement


@admin.register(Counter)
class CounterModelAdmin(admin.ModelAdmin):
    list_display = ["date", "count"]


@admin.register(Announcement)
class AnnouncementModelAdmin(admin.ModelAdmin):
    list_display = ["content", "created"]
