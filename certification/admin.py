from django.contrib import admin
from certification.models import Certification

# Register your models here.
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'c_desc')

admin.site.register(Certification, CertificationAdmin)