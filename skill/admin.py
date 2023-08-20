from django.contrib import admin
from skill.models import Skill

# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    list_display = ('s_id','s_title','s_icon')

admin.site.register(Skill, SkillAdmin)