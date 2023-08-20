from django.contrib import admin
from education.models import Education

# Register your models here.
class EducationAdmin(admin.ModelAdmin):
    list_display = ('e_id', 'e_board', 'e_degree', 'e_marks', 'e_metric')

admin.site.register(Education, EducationAdmin)