# Generated by Django 4.2.4 on 2023-08-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('s_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='S_ID')),
                ('s_title', models.CharField(max_length=250)),
                ('s_icon', models.FileField(default=None, null=True, upload_to='skills/')),
            ],
        ),
    ]