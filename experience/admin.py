from django.contrib import admin
from experience.models import Experience

# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('exp_id', 'exp_title', 'exp_company', 'from_date')

admin.site.register(Experience, ExperienceAdmin)