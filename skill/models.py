from django.db import models

# Create your models here.
class Skill(models.Model):
    s_id = models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='S_ID')
    s_title = models.CharField(max_length=250)
    s_icon = models.FileField(upload_to='skills/', null=True, default=None)