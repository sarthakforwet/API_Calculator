# Generated by Django 3.0.6 on 2020-05-29 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '__first__'),
        ('user', '0002_auto_20200529_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultyprofile',
            name='nature_of_activity',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.Api'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facultyprofile',
            name='self_assesment',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='facultyprofile',
            name='verified_api_score',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.DeleteModel(
            name='FacultyApi',
        ),
    ]
