# Generated by Django 4.1.1 on 2022-10-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='ranking',
            field=models.IntegerField(default=1),
        ),
    ]
