# Generated by Django 4.1.4 on 2022-12-13 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mark1', models.CharField(max_length=30)),
                ('mark2', models.CharField(max_length=30)),
                ('mark3', models.CharField(max_length=30)),
                ('total', models.CharField(max_length=30)),
            ],
        ),
    ]