# Generated by Django 3.0.6 on 2020-05-29 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(choices=[('FOLA/H/SS/L/PEM', 'Faculties of Languages Arts/Humanities/Social Sciences/Library/Physical education/Management'), ('', 'Engineering/Agriculture/Veterinary Science/Sciences/Medical Sciences')], max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]