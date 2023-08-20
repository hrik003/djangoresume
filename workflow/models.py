from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Workflow(models.Model):
    w_id = models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='W_ID')
    w_flow = HTMLField()