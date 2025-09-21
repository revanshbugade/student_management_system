from django.contrib import admin
from .models import StudentsModel
class StudentAdminview(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','course')
admin.site.register(StudentsModel,StudentAdminview)