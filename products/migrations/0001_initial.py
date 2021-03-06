# Generated by Django 3.2 on 2021-04-19 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('price', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('sold_out', models.BooleanField(default=False)),
                ('likes', models.PositiveSmallIntegerField(blank=True, default=0)),
                ('photos', models.FileField(blank=True, default='', upload_to='')),
            ],
        ),
    ]
