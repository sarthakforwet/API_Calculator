# Generated by Django 3.0.6 on 2020-05-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorystream',
            name='stream',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
