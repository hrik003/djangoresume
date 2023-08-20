from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Interest(models.Model):
    i_id = models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='I_ID')
    i_desc = HTMLField()