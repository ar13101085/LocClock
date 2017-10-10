from django.contrib import admin

# Register your models here.
from App.models import Appuser, Schedule

admin.site.register(Appuser)
admin.site.register(Schedule)