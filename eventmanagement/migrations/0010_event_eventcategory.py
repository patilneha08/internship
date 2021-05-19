# Generated by Django 3.0.5 on 2021-05-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanagement', '0009_auto_20210519_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('category', models.CharField(default='', max_length=64)),
                ('date', models.DateTimeField(default='', max_length=64)),
                ('duration', models.DurationField(default='', max_length=64)),
                ('location1', models.CharField(default='', max_length=64)),
                ('location2', models.CharField(default='', max_length=64)),
                ('city', models.CharField(default='', max_length=64)),
                ('state', models.CharField(default='', max_length=64)),
                ('pincode', models.IntegerField(default='', max_length=64)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Eventcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(default='', max_length=64)),
            ],
        ),
    ]
