# Generated by Django 2.2.2 on 2019-06-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('roll', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=20)),
                ('program', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=10)),
                ('hall', models.CharField(max_length=10)),
                ('room', models.CharField(max_length=10)),
                ('blood_group', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('hometown', models.CharField(max_length=10)),
            ],
        ),
    ]
