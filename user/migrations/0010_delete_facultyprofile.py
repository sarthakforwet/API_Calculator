# Generated by Django 3.0.6 on 2020-05-29 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200529_2337'),
        ('user', '0009_auto_20200529_2328'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FacultyProfile',
        ),
    ]
