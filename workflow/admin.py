from django.contrib import admin
from workflow.models import Workflow

# Register your models here.
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('w_id', 'w_flow')

admin.site.register(Workflow, WorkflowAdmin)