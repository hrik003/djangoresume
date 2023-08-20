from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class PersonalInfo(models.Model):
    p_id = models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='P_ID')
    resume_name = models.CharField(max_length=255)
    resume_address = models.CharField(max_length=255)
    resume_phone = models.BigIntegerField()
    resume_email = models.EmailField()
    resume_description = HTMLField()

    def personalinfo_as_list(self):
        return self.resume_name.split(' ')