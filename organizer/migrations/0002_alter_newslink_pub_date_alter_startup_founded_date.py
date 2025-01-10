# Generated by Django 5.1.4 on 2025-01-10 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslink',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='founded_date',
            field=models.DateField(verbose_name='date founded'),
        ),
    ]
