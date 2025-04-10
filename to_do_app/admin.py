from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user__username','date_time_created','status']
    list_select_related = ['user']