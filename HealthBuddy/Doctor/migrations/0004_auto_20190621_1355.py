# Generated by Django 2.2.2 on 2019-06-21 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seven', '0002_auto_20190621_1355'),
        ('Doctor', '0003_auto_20190621_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='vitals',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='seven.bodyVital'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='tests',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seven.Test'),
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]