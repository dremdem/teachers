from django.contrib import admin
from directory.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
