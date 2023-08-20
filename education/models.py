from django.db import models

METRIC_CHOICES = [
    ("CGPA", "CGPA"),
    ("Percentage", "Percentage"),
]

# Create your models here.
class Education(models.Model):
    e_id = models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='E_ID')
    e_board = models.CharField(max_length=255)
    e_institute = models.CharField(max_length=255)
    e_degree = models.CharField(max_length=255)
    e_marks = models.CharField(max_length=25)
    e_metric = models.CharField(max_length=15, choices=METRIC_CHOICES)
    from_date = models.DateField()
    to_date = models.DateField()