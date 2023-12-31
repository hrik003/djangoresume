# Generated by Django 4.2.4 on 2023-08-20 16:17

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('p_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='P_ID')),
                ('resume_name', models.CharField(max_length=255)),
                ('resume_address', models.CharField(max_length=255)),
                ('resume_phone', models.BigIntegerField(max_length=11)),
                ('resume_email', models.EmailField(max_length=254)),
                ('resume_description', tinymce.models.HTMLField()),
            ],
        ),
    ]
