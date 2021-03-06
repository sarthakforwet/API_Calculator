# Generated by Django 3.0.6 on 2020-05-29 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '__first__'),
        ('user', '0005_auto_20200529_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyapi',
            name='nature_of_activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Api'),
        ),
        migrations.AlterField(
            model_name='facultyprofile',
            name='stream',
            field=models.CharField(choices=[('', '----'), ('FOLA/H/SS/L/PEM', 'Faculties of Languages Arts/Humanities/Social Sciences/Library/Physical education/Management'), ('E/A/VS/S/MS', 'Engineering/Agriculture/Veterinary Science/Sciences/Medical Sciences')], max_length=30),
        ),
    ]
