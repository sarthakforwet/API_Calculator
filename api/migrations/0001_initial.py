# Generated by Django 3.0.6 on 2020-05-28 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=500)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature_of_activity', models.CharField(max_length=750)),
                ('max_score', models.PositiveSmallIntegerField()),
                ('self_assesment', models.PositiveSmallIntegerField()),
                ('verified_api_score', models.PositiveSmallIntegerField()),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CategoryStream')),
            ],
        ),
    ]