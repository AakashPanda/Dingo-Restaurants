# Generated by Django 3.0.6 on 2020-07-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_weeklyfeaturedfood_foodimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyfeaturedfood',
            name='foodHour',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
