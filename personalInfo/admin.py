from django.contrib import admin
from personalInfo.models import PersonalInfo

# Register your models here.
class personalInfoAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'resume_name', 'resume_phone', 'resume_email')

admin.site.register(PersonalInfo, personalInfoAdmin)