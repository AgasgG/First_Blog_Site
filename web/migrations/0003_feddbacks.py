# Generated by Django 3.0.5 on 2020-04-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200415_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feddbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('email', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
    ]
