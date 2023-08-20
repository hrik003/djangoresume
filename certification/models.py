from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Certification(models.Model):
    c_id = models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='C_ID')
    c_desc = HTMLField()