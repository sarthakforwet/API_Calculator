# Generated by Django 3.0.6 on 2020-05-29 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '__first__'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyprofile',
            name='stream',
            field=models.CharField(choices=[('', '----'), ('FOLA/H/SS/L/PEM', 'Faculties of Languages Arts/Humanities/Social Sciences/Library/Physical education/Management'), ('', 'Engineering/Agriculture/Veterinary Science/Sciences/Medical Sciences')], max_length=30),
        ),
        migrations.CreateModel(
            name='FacultyApi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_assesment', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('verified_api_score', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('nature_of_activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Api')),
            ],
        ),
    ]
