# Generated by Django 2.2.2 on 2019-06-21 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_patient_emergencycontactrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='emergencyContactRelation',
            field=models.CharField(max_length=20),
        ),
    ]