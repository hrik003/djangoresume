from django.db import models
from tinymce.models import HTMLField

CURRENT_CHOICES = [
    ('No','No'),
    ('Yes', 'Yes'),
]

# Create your models here.
class Experience(models.Model):
    exp_id = models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='EXP_ID')
    exp_title = models.CharField(max_length=255)
    exp_company = models.CharField(max_length=255)
    exp_description = HTMLField()
    from_date = models.DateField()
    exp_current = models.CharField(max_length=15, choices=CURRENT_CHOICES)
    to_date = models.DateField(blank=True, null=True)