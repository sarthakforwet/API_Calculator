# Generated by Django 3.0.6 on 2020-05-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200529_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='self_assesment',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='verified_api_score',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True),
        ),
    ]
