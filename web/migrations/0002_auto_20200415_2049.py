# Generated by Django 3.0.5 on 2020-04-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='datetime',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='publication',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
