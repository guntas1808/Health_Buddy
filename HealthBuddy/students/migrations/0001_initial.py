

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('roll', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=200)),
                ('program', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('hall', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('hometown', models.CharField(max_length=100)),
            ],
        ),
    ]
