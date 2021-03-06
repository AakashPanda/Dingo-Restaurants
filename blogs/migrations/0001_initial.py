# Generated by Django 3.0.6 on 2020-06-27 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsDatabase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True, max_length=50000)),
                ('category', models.CharField(max_length=150)),
                ('postImage', models.ImageField(blank=True, null=True, upload_to='Blogs')),
                ('slug', models.CharField(blank=True, max_length=50)),
                ('timeStamp', models.DateTimeField(default=datetime.datetime.utcnow, null=True)),
            ],
        ),
    ]
